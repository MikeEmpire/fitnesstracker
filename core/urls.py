from django.urls import path, include

urlpatterns = [
    path("", include("core.url_patterns.user_urls")),
    path("", include("core.url_patterns.workout_urls")),
    path("", include("core.url_patterns.nutrition_urls")),
    path("", include("core.url_patterns.tracking_urls")),
]
