from rest_framework.generics import get_object_or_404

from .models import Step, FinalStep, Choice
from .serializers import StepSerializer, FinalStepSerializer, ChoiceSerializer
from rest_framework import viewsets, generics


class StepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

    def get_queryset(self):
        queryset = Step.objects.all()
        is_first_step = self.request.query_params.get('is_first_step', None)
        if is_first_step is not None:
            # TODO: return one only!
            queryset = queryset.filter(is_first_step=is_first_step)
        return queryset


class FinalStepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FinalStep.objects.all()
    serializer_class = FinalStepSerializer


class ChoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
