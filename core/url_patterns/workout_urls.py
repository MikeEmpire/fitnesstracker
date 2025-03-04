from django.urls import path
from core.views.workout_views import WorkoutPlanView


urlpatterns = [
    path("workout/", WorkoutPlanView.as_view(), name="workouts"),
]
