from rest_framework import serializers
from .models import Step, FirstStep, FinalStep, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    answer_id = serializers.ChoiceField(choices=Choice.objects.all(), write_only=True)
    answer = serializers.CharField(source='get_answer_display', read_only=True)

    class Meta:
        model = Choice
        fields = ('id', 'answer', 'answer_id', 'additional_answer_text', 'step', 'next_step')
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


class FirstStepSerializer(serializers.ModelSerializer):
    step = StepSerializer()

    class Meta:
        model = FirstStep
        fields = ('step', )
