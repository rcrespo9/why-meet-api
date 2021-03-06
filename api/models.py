from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.db import models


class Step(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['is_first_step'], condition=Q(is_first_step=True), name="one_first_step")
        ]

    text = models.TextField(unique=True)
    is_first_step = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Choice(models.Model):
    # TODO: inverse of step and next step can't exist
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['step', 'next_step'], name='unique_step_next_step')
        ]

    class Answer(models.IntegerChoices):
        NO = 0, _('No')
        YES = 1, _('Yes')

    answer = models.IntegerField(choices=Answer.choices)
    additional_answer_text = models.CharField(max_length=100, null=True, blank=True)
    step = models.ForeignKey(Step, related_name="choices", on_delete=models.CASCADE)
    next_step = models.ForeignKey(Step, null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if self.next_step is not None:
            if self.step.pk == self.next_step.pk:
                raise ValidationError("Parent step and next step can't be the same.")

        if hasattr(self.step, "final_step"):
            raise ValidationError("Final steps can't have any choices.")

        if hasattr(self.step, "interstitial_step"):
            raise ValidationError("Interstitial steps can't have any choices.")

        return super(Choice, self).save(*args, **kwargs)

    def __str__(self):
        return '%s - %s -> %s' % (self.step.text, self.get_answer_display(), self.next_step.text)


class InterstitialStep(models.Model):
  step = models.OneToOneField(
      Step, primary_key=True, related_name="interstitial_step", on_delete=models.CASCADE)
  next_step = models.OneToOneField(
      Step, null=True, blank=True, on_delete=models.SET_NULL)

  def save(self, *args, **kwargs):
    if self.step.choices.exists():
        raise ValidationError("Interstitial steps can't have any choices.")

    if hasattr(self.step, "final_step"):
        raise ValidationError("Final steps can't be interstitial steps.")

    if self.step.is_first_step:
        raise ValidationError("Interstitial step can't be first step.")
    return super(FinalStep, self).save(*args, **kwargs)

  def __str__(self):
    return self.step.text


class FinalStep(models.Model):
    step = models.OneToOneField(Step, primary_key=True, related_name="final_step", on_delete=models.CASCADE)
    should_go_to_meeting = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.step.choices.exists():
            raise ValidationError("Final steps can't have any choices.")

        if hasattr(self.step, "interstitial_step"):
            raise ValidationError("Interstitial steps can't be final steps.")

        if self.step.is_first_step:
            raise ValidationError("Final step can't be first step.")
        return super(FinalStep, self).save(*args, **kwargs)

    def __str__(self):
        return self.step.text
