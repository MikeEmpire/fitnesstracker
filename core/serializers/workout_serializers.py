from rest_framework import serializers
from core.models.workout_models import WorkoutPlan

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = "__all__"
