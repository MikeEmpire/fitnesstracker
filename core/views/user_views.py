from core.models.user_models import User
from core.serializers.user_serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class UserListView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
