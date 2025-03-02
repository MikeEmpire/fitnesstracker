from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views.workout_views import WorkoutPlanViewSet

router = DefaultRouter()
router.register(r'workout-plans', WorkoutPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
