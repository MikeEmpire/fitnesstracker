from core.models.workout_models import WorkoutPlan
from core.serializers.workout_serializers import WorkoutPlanSerializer
from django.views import View
from rest_framework.response import Response


class WorkoutPlanView(View):
    def get(self, request, *args, **kwargs):
        plans = WorkoutPlan.objects.all()
        serializer = WorkoutPlanSerializer(plans, many=True)
        return Response(serializer.data)
