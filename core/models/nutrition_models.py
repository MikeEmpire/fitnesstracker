from django.db import models
from .user_models import User


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
