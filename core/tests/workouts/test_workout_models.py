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
    assert plan.deleted_at is None


@pytest.mark.django_db
def test_default_duration(test_user):
    """Ensure the default duration is set correctly if not provided"""
    plan = WorkoutPlan.objects.create(
        user=test_user, name="General Plan", goal="fitness"
    )

    assert plan.duration == 4


@pytest.mark.django_db
def test_delete_workout_plan(test_user):
    """Test to make sure that a WorkoutPlan is deleted"""
    plan = WorkoutPlan.objects.create(
        user=test_user, name="General Plan", goal="fitness"
    )

    plan.delete()

    assert not WorkoutPlan.objects.filter(id=plan.id).exists()


@pytest.mark.django_db
def test_update_workout_plan(test_user):
    """Test to make sure that you can edit a workout plan"""
    plan = WorkoutPlan.objects.create(
        user=test_user, name="General Plan", goal="fitness"
    )
    plan.name = "Test workout plan"
    plan.save(update_fields=["name"])

    updated_object = WorkoutPlan.objects.filter(id=plan.id).first()

    assert updated_object.name == "Test workout plan"


@pytest.mark.django_db
def test_invalid_workout_plan_goal(test_user):
    """Test to make sure that you can't set an invalid goal"""
