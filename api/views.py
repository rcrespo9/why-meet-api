from .models import Step, FirstStep, FinalStep, Choice
from .serializers import FirstStepSerializer, StepSerializer, FinalStepSerializer, ChoiceSerializer
from rest_framework import viewsets


class StepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class FirstStepViewSet(viewsets.ReadOnlyModelViewSet):
    # TODO: only get first step since there should only be one
    queryset = FirstStep.objects.all()
    serializer_class = FirstStepSerializer


class FinalStepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FinalStep.objects.all()
    serializer_class = FinalStepSerializer


class ChoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
