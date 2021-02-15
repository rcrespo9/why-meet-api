from django.db import models
from django.db.models import UniqueConstraint


class Step(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Choice(models.Model):
    class Answer(models.IntegerChoices):
        NO = 0, 'No'
        YES = 1, 'Yes'

    answer = models.IntegerField(choices=Answer.choices)
    additional_answer_text = models.CharField(max_length=100, blank=True, null=True)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


class NextStep(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['step', 'choice'], name='step_choice')
        ]

    step = models.OneToOneField(Step, primary_key=True, on_delete=models.CASCADE)
    choice = models.OneToOneField(Choice, on_delete=models.CASCADE)


class InterstitialStep(models.Model):
    step = models.OneToOneField(Step, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.step.text


class FirstStep(models.Model):
    step = models.OneToOneField(Step, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.step.text


class FinalStep(models.Model):
    step = models.OneToOneField(Step, primary_key=True, on_delete=models.CASCADE)
    is_go = models.BooleanField(default=False)

    def __str__(self):
        return self.step.text
