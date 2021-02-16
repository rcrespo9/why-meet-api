from rest_framework import serializers
from .models import Step, FirstStep, Choice


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('answer', 'additional_answer_text', 'step', 'next_step')


class StepSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Step
        fields = ('id', 'text', 'choices')


class FirstStepSerializer(serializers.ModelSerializer):
    step = StepSerializer()

    class Meta:
        model = FirstStep
        fields = ('step', )
