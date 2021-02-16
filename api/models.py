from django.db import models


class Step(models.Model):
    text = models.TextField()
    is_interstitial = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Choice(models.Model):
    class Answer(models.IntegerChoices):
        NO = 0, 'No'
        YES = 1, 'Yes'

    answer = models.IntegerField(choices=Answer.choices)
    additional_answer_text = models.CharField(max_length=100, null=True)
    step = models.ForeignKey(Step, related_name="choices", on_delete=models.CASCADE)
    next_step = models.OneToOneField(Step, related_name="next_step", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.answer


class FirstStep(models.Model):
    step = models.OneToOneField(Step, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.step.text


class FinalStep(models.Model):
    step = models.OneToOneField(Step, primary_key=True, on_delete=models.CASCADE)
    is_go = models.BooleanField(default=False)

    def __str__(self):
        return self.step.text
