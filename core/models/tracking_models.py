from django.db import models
from core.models.user_models import User


class Checklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checklists")
    date = models.DateField()
    workout_completed = models.BooleanField(default=False)
    meals_followed = models.BooleanField(default=False)
