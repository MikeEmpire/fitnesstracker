import pytest
from core.models.workout_models import (
    WorkoutPlan,
    WorkoutSession,
    Exercise,
    WorkoutPreferences,
)
from core.serializers.workout_serializers import (
    WorkoutPlanSerializer,
    WorkoutPreferencesSerializer,
    ExerciseSerializer,
    WorkoutSessionSerializer,
)


@pytest.mark.django_db
def test_serialized_output_with_sessions(test_user):
    """Ensure that workout sessions are correctly serialized within a workout plan."""

    plan = WorkoutPlan.objects.create(
        user=test_user, name="Strength Plan", goal="strength", duration=6
    )

    WorkoutSession.objects.create(
        workout_plan=plan, name="Monday", day_of_week="monday"
    )
    WorkoutSession.objects.create(
        workout_plan=plan, name="Tuesday", day_of_week="tuesday"
    )

    serializer = WorkoutPlanSerializer(plan)

    expected_data = {
        "id": plan.id,
        "name": "Strength Plan",
        "goal": "strength",
        "workout_sessions": [
            {"day_of_week": "monday", "exercises": [], "id": 1, "name": "Monday"},
            {"day_of_week": "tuesday", "exercises": [], "id": 2, "name": "Tuesday"},
        ],
        "created_at": plan.created_at.astimezone()
        .isoformat(timespec="microseconds")
        .replace("+00:00", "Z"),
        "updated_at": plan.updated_at.astimezone()
        .isoformat(timespec="microseconds")
        .replace("+00:00", "Z"),
        "deleted_at": None,
        "duration": 6,
    }

    assert serializer.data == expected_data


@pytest.mark.django_db
def test_serialized_output_without_sessions(test_user):
    """Ensure that a workout plan without sessions serializes correctly"""

    plan = WorkoutPlan.objects.create(
        user=test_user, name="Strength Plan", goal="strength", duration=6
    )

    serializer = WorkoutPlanSerializer(plan)

    expected_data = {
        "id": plan.id,
        "name": "Strength Plan",
        "goal": "strength",
        "workout_sessions": [],
        "created_at": plan.created_at.astimezone()
        .isoformat(timespec="microseconds")
        .replace("+00:00", "Z"),
        "updated_at": plan.updated_at.astimezone()
        .isoformat(timespec="microseconds")
        .replace("+00:00", "Z"),
        "deleted_at": None,
        "duration": 6,
    }

    assert serializer.data == expected_data


@pytest.mark.django_db
def test_invalid_workout_plan_serializer():
    """Ensure validation fails when required fields are missing"""

    invalid_data = {"name": "Leg Day Plan"}

    serializer = WorkoutPlanSerializer(data=invalid_data)
    assert serializer.is_valid() is False
    assert "goal" in serializer.errors


@pytest.mark.django_db
def test_valid_exercises_serializer(test_user):
    """Ensure that exercises are correctly serialized within a workout session"""
    plan = WorkoutPlan.objects.create(
        user=test_user, name="Strength Plan", goal="strength", duration=6
    )
    workout_session = WorkoutSession.objects.create(
        workout_plan=plan, name="Tuesday", day_of_week="tuesday"
    )
    exercise = Exercise.objects.create(
        workout_session=workout_session,
        name="Test Exercise",
        sets=2,
        reps=4,
        rest_time=30,
        equipment_needed="Tools",
        muscle_group=["chest", "back"],
    )

    serializer = ExerciseSerializer(exercise)
    expected_data = {
        "id": exercise.id,
        "name": "Test Exercise",
        "sets": 2,
        "reps": 4,
        "rest_time": 30,
        "equipment_needed": "Tools",
        "muscle_group": ["chest", "back"],
        "workout_session": workout_session.id,
    }

    assert serializer.data == expected_data


@pytest.mark.django_db
def test_invalid_exercise_serializer():
    """Ensure validation fails when required fields are missing"""
    invalid_data = {"name": "Test Exercise"}

    serializer = ExerciseSerializer(data=invalid_data)
    assert serializer.is_valid() is False


@pytest.mark.django_db
def test_valid_workout_preferences_serializer(test_user):
    """Ensure that workout preferences are correctly serialized"""
    preferences = WorkoutPreferences.objects.create(
        user=test_user,
        workout_location="gym",
        available_equipment=["dumbbells", "resistance bands", "pull-up bar"],
        fitness_goal="weight_loss",
        experience_level="beginner",
        days_per_week=4,
        health_conditions="None",
    )

    serializer = WorkoutPreferencesSerializer(preferences)

    expected_data = {
        "id": preferences.id,
        "workout_location": "gym",
        "available_equipment": ["dumbbells", "resistance bands", "pull-up bar"],
        "fitness_goal": "weight_loss",
        "experience_level": "beginner",
        "days_per_week": 4,
        "health_conditions": "None",
    }

    assert serializer.data == expected_data


@pytest.mark.django_db
def test_invalid_workout_preferences_serializer():
    """Ensure that the workout preferences serializer raises errors for improper JSON structure"""

    invalid_data = {"workout_location": "gym"}

    serializer = WorkoutPreferencesSerializer(data=invalid_data)
    assert serializer.is_valid() is False
    assert "fitness_goal" in serializer.errors


@pytest.mark.django_db
def test_valid_workout_session_serializer(test_user):
    """Ensure that the workout session serializer works properly"""

    plan = WorkoutPlan.objects.create(
        user=test_user, name="Strength Plan", goal="strength", duration=6
    )
    workout_session = WorkoutSession.objects.create(
        workout_plan=plan, name="Tuesday", day_of_week="tuesday"
    )
    serializer = WorkoutSessionSerializer(workout_session)

    expected_data = {
        "id": workout_session.id,
        "name": "Tuesday",
        "day_of_week": "tuesday",
        "created_at": workout_session.created_at.astimezone()
        .isoformat(timespec="microseconds")
        .replace("+00:00", "Z"),
        "updated_at": workout_session.updated_at.astimezone()
        .isoformat(timespec="microseconds")
        .replace("+00:00", "Z"),
        "deleted_at": None,
    }
    
    assert serializer.data == expected_data
    
