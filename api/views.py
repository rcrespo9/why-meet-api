from rest_framework.views import APIView
from .models import Step, FinalStep, Choice
from .serializers import StepSerializer, FinalStepSerializer, ChoiceSerializer
from rest_framework import response, viewsets


class StepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class FirstStep(viewsets.ReadOnlyModelViewSet):
  queryset = Step.objects.filter(is_first_step=True).distinct()
  serializer_class = StepSerializer


class FinalStepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FinalStep.objects.all()
    serializer_class = FinalStepSerializer


class ChoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
