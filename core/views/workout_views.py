from rest_framework import viewsets
from core.models.workout_models import WorkoutPlan
from core.serializers.workout_serializers import WorkoutPlanSerializer

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
