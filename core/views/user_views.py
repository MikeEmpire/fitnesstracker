from core.models.user_models import User
from core.serializers.user_serializers import UserSerializer
from django.views import View
from rest_framework.response import Response


# Create your views here.
class UserView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
