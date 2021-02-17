from .models import Step, FirstStep, FinalStep, Choice
from .serializers import FirstStepSerializer, StepSerializer, FinalStepSerializer, ChoiceSerializer
from rest_framework import viewsets


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class FirstStepViewSet(viewsets.ModelViewSet):
    queryset = FirstStep.objects.all()
    serializer_class = FirstStepSerializer


class FinalStepViewSet(viewsets.ModelViewSet):
    queryset = FinalStep.objects.all()
    serializer_class = FinalStepSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
