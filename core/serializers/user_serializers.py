from rest_framework import serializers
from core.models.user_models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "fitness_goal",
            "workout_location",
            "dietary_preferences",
            "height",
            "weight",
        ]
