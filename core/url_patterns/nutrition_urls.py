from core.views.nutrition_views import NutritionPlanView
from django.urls import path

urlpatterns = [
    path("nutrition-plans/", NutritionPlanView.as_view(), name="nutrition plans")
]
