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

    text = models.TextField()
    is_interstitial = models.BooleanField(default=False)
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
        YES = 1, _('Yes'),
        NA = 2, _('Not Applicable')

    answer = models.IntegerField(choices=Answer.choices)
    additional_answer_text = models.CharField(max_length=100, null=True, blank=True)
    step = models.ForeignKey(Step, related_name="choices", on_delete=models.CASCADE)
    next_step = models.ForeignKey(Step, null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if self.next_step is not None:
            if self.step.pk == self.next_step.pk:
                raise ValidationError("Parent step and next step can't be the same.")

        if self.step.is_interstitial and (self.answer != 2 or self.additional_answer_text is not None):
            raise ValidationError("The only answer allowed for interstitial steps is N/A.")

        # TODO: there can't exist inverse version of steps

        if hasattr(self.step, "final_step"):
            raise ValidationError("Final steps can't have any choices.")

        return super(Choice, self).save(*args, **kwargs)

    def __str__(self):
        return '%s - %s' % (self.step.text, self.get_answer_display())


class FinalStep(models.Model):
    step = models.OneToOneField(Step, primary_key=True, related_name="final_step", on_delete=models.CASCADE)
    should_go_to_meeting = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.step.choices.exists():
            raise ValidationError("Final steps can't have any choices.")

        if self.step.is_interstitial:
            raise ValidationError("Interstitial steps can't be final steps.")

        if self.step.is_first_step:
            raise ValidationError("Final step can't be first step.")
        return super(FinalStep, self).save(*args, **kwargs)

    def __str__(self):
        return self.step.text
