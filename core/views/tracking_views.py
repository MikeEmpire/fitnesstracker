from django.views import View
from core.models.tracking_models import Checklist
from core.serializers.tracking_serializers import ChecklistSerializer
from rest_framework.response import Response


class ChecklistView(View):
    def get(self, request, *args, **kwargs):
        checklists = Checklist.objects.all()
        serializer = ChecklistSerializer(checklists, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ChecklistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
