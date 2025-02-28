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


class NutritionPlan(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="nutrition_plans"
    )
    daily_calories = models.IntegerField()
    protein_g = models.FloatField()
    carbs_g = models.FloatField()
    fats_g = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Meal(models.Model):
    nutrition_plan = models.ForeignKey(
        NutritionPlan, on_delete=models.CASCADE, related_name="meals"
    )
    name = models.CharField(max_length=255)
    calories = models.IntegerField()
    protein_g = models.FloatField()
    carbs_g = models.FloatField()
    fats_g = models.FloatField()
    meal_type = models.CharField(
        max_length=50,
        choices=[
            ("breakfast", "Breakfast"),
            ("lunch", "Lunch"),
            ("dinner", "Dinner"),
            ("snack", "Snack"),
        ],
    )


class Checklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checklists")
    date = models.DateField()
    workout_completed = models.BooleanField(default=False)
    meals_followed = models.BooleanField(default=False)
