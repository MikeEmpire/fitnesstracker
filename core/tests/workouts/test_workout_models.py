import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from core.models.workout_models import Exercise, WorkoutPlan, WorkoutSession


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
        user=test_user, name="General Plan", goal="strength"
    )

    assert plan.duration == 4


@pytest.mark.django_db
def test_delete_workout_plan(test_user):
    """Test to make sure that a WorkoutPlan is deleted"""
    plan = WorkoutPlan.objects.create(
        user=test_user, name="General Plan", goal="strength"
    )

    plan.delete()

    assert not WorkoutPlan.objects.filter(id=plan.id).exists()


@pytest.mark.django_db
def test_update_workout_plan(test_user):
    """Test to make sure that you can edit a workout plan"""
    plan = WorkoutPlan.objects.create(
        user=test_user, name="General Plan", goal="strength"
    )
    plan.name = "Test workout plan"
    plan.save(update_fields=["name"])

    updated_object = WorkoutPlan.objects.filter(id=plan.id).first()

    assert updated_object.name == "Test workout plan"


@pytest.mark.django_db
def test_invalid_workout_plan_goal(test_user):
    """Test to make sure that you can't set an invalid goal"""
    with pytest.raises(ValidationError, match="is not a valid goal"):
        WorkoutPlan.objects.create(
            user=test_user, name="Invalid Plan", goal="invalid_goal", duration=6
        )


@pytest.mark.django_db
def test_create_workout_session(test_user):
    """Create a new workout session properly"""
    plan = WorkoutPlan.objects.create(
        user=test_user, name="General Plan", goal="strength"
    )
    workout_session = WorkoutSession.objects.create(
        workout_plan=plan, name="Test Session", day_of_week="monday"
    )

    assert workout_session.id is not None
    assert workout_session.name == "Test Session"
    assert workout_session.deleted_at is None
    assert workout_session.day_of_week == "monday"
    assert workout_session.workout_plan == plan
    assert workout_session.workout_plan.id == plan.id


@pytest.mark.django_db
def test_invalid_workout_session_without_plan(test_user):
    """Test to make sure that you can't create a workout session without a plan"""
    with pytest.raises(IntegrityError, match='null value in column "workout_plan_id"'):
        WorkoutSession.objects.create(
            workout_plan=None, name="Test Session", day_of_week="monday"
        )


@pytest.mark.django_db
def test_create_exercise_model(test_user):
    """Test to make sure that an exercise is created properly"""
    plan = WorkoutPlan.objects.create(
        user=test_user, name="General Plan", goal="strength"
    )
    session = WorkoutSession.objects.create(
        workout_plan=plan, name="Test Session", day_of_week="monday"
    )
    exercise = Exercise.objects.create(
        workout_session=session,
        name="Test Exercise",
        reps=10,
        sets=3,
        rest_time=30,
        equipment_needed="Tools",
        muscle_group=["chest", "back"],
    )

    assert exercise.id is not None
    assert exercise.name == "Test Exercise"
    assert exercise.reps == 10
    assert exercise.sets == 3
    assert exercise.workout_session == session
    assert exercise.workout_session.id == session.id


@pytest.mark.django_db
def test_invalid_exercise_model_without_session(test_user):
    """Test to make sure that you can't create an exercise without a session"""
    with pytest.raises(
        IntegrityError, match='null value in column "workout_session_id"'
    ):
        Exercise.objects.create(
            workout_session=None,
            name="Test Exercise",
            reps=10,
            sets=3,
            rest_time=30,
            equipment_needed="Tools",
            muscle_group=["chest", "back"],
        )
