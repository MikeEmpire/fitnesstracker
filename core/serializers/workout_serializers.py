from rest_framework import serializers
from core.models.workout_models import WorkoutPlan, WorkoutSession, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "name", "sets", "reps", "rest_time", "muscle_group"]


class WorkoutSessionSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutSession
        fields = ["id", "name", "day_of_week", "exercises"]


class WorkoutPlanSerializer(serializers.ModelSerializer):
    workout_sessions = WorkoutSessionSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ["id", "name", "goal", "created_at", "workout_sessions"]
