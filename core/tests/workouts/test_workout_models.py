from django.test import TestCase
from core.models.workout_models import WorkoutPlan
from core.models.user_models import User


class WorkoutPlanModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")

    def test_create_workout_plan(self):
        plan = WorkoutPlan.objects.create(
            user=self.user, name="Beginner Plan", goal="strength", duration=8
        )
        self.assertEqual(plan.name, "Beginner Plan")
