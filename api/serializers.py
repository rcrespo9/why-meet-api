from rest_framework import serializers
from .models import Step, FinalStep, Choice, InterstitialStep


class ChoiceSerializer(serializers.ModelSerializer):
    answer = serializers.CharField(source='get_answer_display')

    class Meta:
        model = Choice
        fields = ('id', 'answer', 'additional_answer_text', 'next_step')


class FinalStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalStep
        fields = ('should_go_to_meeting',)


class InterstitialStepSerializer(serializers.ModelSerializer):
    class Meta:
      model = InterstitialStep
      fields = ('next_step', )


class StepSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    final_step = FinalStepSerializer()
    interstitial_step = InterstitialStepSerializer()

    class Meta:
        model = Step
        fields = ('text', 'choices', 'final_step', 'is_first_step', 'interstitial_step')
