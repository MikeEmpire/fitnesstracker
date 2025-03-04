from django.views import View
from core.models.nutrition_models import NutritionPlan
from core.serializers.nutrition_serializers import NutritionPlanSerializer
from rest_framework.response import Response


class NutritionPlanView(View):
    def get(self, request, *args, **kwargs):
        nutrition_plans = NutritionPlan.objects.all()
        serializer = NutritionPlanSerializer(nutrition_plans, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = NutritionPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
