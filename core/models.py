from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    fitness_goal = models.CharField(
        max_length=100,
        choices=[
            ("weight_loss", "Weight Loss"),
            ("muscle_gain", "Muscle Gain"),
            ("endurance", "Endurance"),
            ("general_fitness", "General Fitness"),
        ],
        default="general_fitness",
    )
    workout_location = models.CharField(
        max_length=50, choices=[("home", "Home"), ("gym", "Gym")], default="gym"
    )
    dietary_preferences = models.TextField(
        blank=True, null=True
    )  # JSON for diet preferences
    height = models.FloatField(null=True, blank=True)  # in cm
    weight = models.FloatField(null=True, blank=True)  # in kg

