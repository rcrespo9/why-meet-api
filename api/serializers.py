from rest_framework import serializers
from .models import Step, FirstStep, FinalStep, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    answer_id = serializers.ChoiceField(choices=Choice.objects.all(), write_only=True)
    answer = serializers.CharField(source='get_answer_display', read_only=True)

    class Meta:
        model = Choice
        fields = ('id', 'answer', 'answer_id', 'additional_answer_text', 'step', 'next_step')


class FinalStepSerializer(serializers.ModelSerializer):
    step_text = serializers.CharField(source="step.text", read_only=True)

    class Meta:
        model = FinalStep
        fields = ('step', 'step_text', 'should_go_to_meeting')


class StepSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    final_step = FinalStepSerializer(read_only=True)

    class Meta:
        model = Step
        fields = ('id', 'text', 'choices', 'final_step')


class FirstStepSerializer(serializers.ModelSerializer):
    step = StepSerializer(read_only=True)
    step_id = serializers.PrimaryKeyRelatedField(
        queryset=Step.objects.all(),
        source="step",
        required=True,
        write_only=True
    )

    class Meta:
        model = FirstStep
        fields = ('step', 'step_id')
