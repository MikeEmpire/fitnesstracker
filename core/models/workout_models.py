from django.db import models
from core.models.user_models import User


class WorkoutPlan(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="workout_plans"
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    goal = models.CharField(
        max_length=100,
        choices=[
            ("strength", "Strength"),
            ("cardio", "Cardio"),
            ("hypertrophy", "Hypertrophy"),
            ("fat_loss", "Fat Loss"),
        ],
    )
    duration = models.IntegerField(default=4)


class WorkoutSession(models.Model):
    workout_plan = models.ForeignKey(
        WorkoutPlan, on_delete=models.CASCADE, related_name="workout_sessions"
    )
    name = models.CharField(max_length=255)
    day_of_week = models.CharField(
        max_length=10,
        choices=[
            ("monday", "Monday"),
            ("tuesday", "Tuesday"),
            ("wednesday", "Wednesday"),
            ("thursday", "Thursday"),
            ("friday", "Friday"),
            ("saturday", "Saturday"),
            ("sunday", "Sunday"),
        ],
    )


class Exercise(models.Model):
    workout_session = models.ForeignKey(
        WorkoutSession, on_delete=models.CASCADE, related_name="exercises"
    )
    name = models.CharField(max_length=255)
    sets = models.PositiveIntegerField(default=2)
    reps = models.PositiveIntegerField(default=10)
    rest_time = models.PositiveIntegerField(default=60)  # in seconds
    equipment_needed = models.CharField(max_length=255, blank=True, null=True)
    muscle_group = models.CharField(
        max_length=100,
        choices=[
            ("chest", "Chest"),
            ("back", "Back"),
            ("legs", "Legs"),
            ("arms", "Arms"),
            ("shoulders", "Shoulders"),
            ("abs", "Abs"),
            ("core", "Core"),
            ("other", "Other"),
            ("none", "None"),
            ("full_body", "Full Body"),
        ],
        default="none",
    )


class WorkoutPreferences(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="preferences"
    )
    workout_location = models.CharField(
        max_length=10, choices=[("gym", "Gym"), ("home", "Home")]
    )
    available_equipment = models.JSONField(
        default=list
    )  # List of equipment for home workouts
    fitness_goal = models.CharField(
        max_length=50,
        choices=[
            ("weight_loss", "Weight Loss"),
            ("muscle_gain", "Muscle Gain"),
            ("endurance", "Endurance"),
            ("general_fitness", "General Fitness"),
        ],
    )
    experience_level = models.CharField(
        max_length=20,
        choices=[
            ("beginner", "Beginner"),
            ("intermediate", "Intermediate"),
            ("advanced", "Advanced"),
        ],
    )
    days_per_week = models.IntegerField(default=3)
    health_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Preferences"
