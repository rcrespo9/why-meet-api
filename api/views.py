from .models import Step, FinalStep, Choice
from .serializers import StepSerializer, FinalStepSerializer, ChoiceSerializer
from rest_framework import viewsets


class StepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class FinalStepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FinalStep.objects.all()
    serializer_class = FinalStepSerializer


class ChoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
