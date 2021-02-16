from .models import Step, FirstStep, Choice
from .serializers import FirstStepSerializer, StepSerializer, ChoiceSerializer
from rest_framework import viewsets


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class FirstStepViewSet(viewsets.ModelViewSet):
    queryset = FirstStep.objects.all()
    serializer_class = FirstStepSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
