from core.decorators.validate_json import validate_json
from core.models.workout_models import (
    WorkoutPlan,
)
from core.serializers.workout_serializers import (
    WorkoutPlanSerializer,
    WorkoutPreferencesSerializer,
)
from core.services.workout_services import generate_workout_plan
from core.types import WorkoutPreferences
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from rest_framework.views import APIView


class WorkoutPlanView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all workout plans.",
        responses={200: WorkoutPlanSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        plans = WorkoutPlan.objects.all()
        serializer = WorkoutPlanSerializer(plans, many=True)
        return Response({"data": serializer.data}, status=HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Delete a workout plan.",
    )
    def delete(self, request, *args, **kwargs):
        plan_id = kwargs.get("plan_id")
        plan = WorkoutPlan.objects.filter(id=plan_id).first()
        if plan:
            plan.delete()
            return Response({"message": "Workout plan deleted"}, status=HTTP_200_OK)
        return Response({"error": "Workout plan not found"}, status=HTTP_404_NOT_FOUND)


class GenerateWorkoutPlanView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Generate a workout plan")
    @validate_json(WorkoutPreferences)
    def post(self, request, *args, **kwargs):
        user = request.user
        workout_preferences = request.data

        plan = generate_workout_plan(user, workout_preferences)
        return Response(
            {"message": "Workout plan generated", "plan_id": plan.id},
            status=HTTP_201_CREATED,
        )


class WorkoutPreferencesView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Save a user's workout preferences")
    def post(self, request, *args, **kwargs):
        serializer = WorkoutPreferencesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
