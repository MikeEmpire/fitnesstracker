from core.decorators.validate_json import validate_json
from core.models.workout_models import WorkoutPlan
from core.serializers.workout_serializers import WorkoutPlanSerializer
from core.services.workout_services import generate_workout_plan
from core.types import WorkoutPreferences
from rest_framework.response import Response
from rest_framework.views import APIView


class WorkoutPlanView(APIView):
    def get(self, request, *args, **kwargs):
        plans = WorkoutPlan.objects.all()
        serializer = WorkoutPlanSerializer(plans, many=True)
        return Response(serializer.data)


class GenerateWorkoutPlanView(APIView):
    @validate_json(WorkoutPreferences)
    def post(self, request, *args, **kwargs):
        preferences: WorkoutPreferences = request.data

        plan = generate_workout_plan(preferences)
        return Response({"message": "Workout plan generated", "plan_id": plan.id})
