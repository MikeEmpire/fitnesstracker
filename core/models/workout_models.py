from django.db import models
from core.models.user_models import User

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout_plans")
    name = models.CharField(max_length=255)
    goal = models.CharField(max_length=100)
    duration = models.IntegerField(default=4)
