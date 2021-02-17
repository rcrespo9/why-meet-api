from rest_framework import serializers
from .models import Step, FirstStep, FinalStep, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('answer', 'additional_answer_text', 'step', 'next_step')


class FinalStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalStep
        fields = ('step', 'should_go_to_meeting')


class StepSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    final_step = FinalStepSerializer(read_only=True)

    class Meta:
        model = Step
        fields = ('id', 'text', 'choices', 'final_step')


class FirstStepSerializer(serializers.ModelSerializer):
    # step = StepSerializer()

    class Meta:
        model = FirstStep
        fields = ('step', )
