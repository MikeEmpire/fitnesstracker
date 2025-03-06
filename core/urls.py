from django.urls import path, include

urlpatterns = [
    path("auth/", include("core.url_patterns.auth_urls")),
    path("users/", include("core.url_patterns.user_urls")),
    path("workouts/", include("core.url_patterns.workout_urls")),
    path("nutrition/", include("core.url_patterns.nutrition_urls")),
    path("tracking/", include("core.url_patterns.tracking_urls")),
]
