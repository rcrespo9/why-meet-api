from rest_framework import serializers
from .models import Step, FinalStep, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    answer = serializers.CharField(source='get_answer_display')

    class Meta:
        model = Choice
        fields = ('id', 'answer', 'additional_answer_text', 'step', 'next_step')
        depth = 1


class FinalStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalStep
        fields = ('step', 'should_go_to_meeting')


class StepSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    final_step = FinalStepSerializer()

    class Meta:
        model = Step
        fields = ('id', 'text', 'choices', 'final_step')
