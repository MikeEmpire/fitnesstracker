import pytest
from core.models.workout_models import WorkoutPlan


@pytest.mark.django_db
def test_create_workout_plan(test_user):
    """Ensure a WorkoutPlan is created successfully"""
    plan = WorkoutPlan.objects.create(
        user=test_user, name="Strength Plan", goal="strength", duration=6
    )

    assert plan.id is not None
    assert plan.name == "Strength Plan"
    assert plan.goal == "strength"
    assert plan.duration == 6


@pytest.mark.django_db
def test_default_duration(test_user):
    """Ensure the default duration is set correctly if not provided"""
    plan = WorkoutPlan.objects.create(
        user=test_user, name="General Plan", goal="fitness"
    )

    assert plan.duration == 4
