from django.urls import path
from core.views.workout_views import (
    WorkoutPreferencesView,
    GenerateWorkoutPlanView,
    WorkoutPlanView,
)


urlpatterns = [
    path("", WorkoutPlanView.as_view(), name="workouts"),
    path(
        "generate-workout/",
        GenerateWorkoutPlanView.as_view(),
        name="Generate Workout Plans",
    ),
    path("preferences/", WorkoutPreferencesView.as_view(), name="Workout preferences"),
]
