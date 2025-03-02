from rest_framework import viewsets
from core.models.user_models import User
from core.serializers.user_serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
