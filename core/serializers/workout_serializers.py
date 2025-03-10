from rest_framework import serializers
from core.models.workout_models import (
    WorkoutPlan,
    WorkoutSession,
    Exercise,
    WorkoutPreferences,
)


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            "id",
            "name",
            "sets",
            "reps",
            "rest_time",
            "muscle_group",
            "equipment_needed",
            "workout_session",
        ]


class WorkoutSessionSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutSession
        fields = [
            "id",
            "exercises",
            "name",
            "day_of_week",
            "deleted_at",
            "created_at",
            "updated_at",
        ]


class WorkoutPlanSerializer(serializers.ModelSerializer):
    workout_sessions = WorkoutSessionSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = [
            "id",
            "name",
            "goal",
            "created_at",
            "workout_sessions",
            "duration",
            "deleted_at",
            "created_at",
            "updated_at",
        ]


class WorkoutPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPreferences
        fields = [
            "id",
            "fitness_goal",
            "available_equipment",
            "experience_level",
            "days_per_week",
            "health_conditions",
            "workout_location",
        ]
