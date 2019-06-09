from rest_framework import serializers

from auth_api.models import User


class BaseUserSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер модели User."""

    class Meta:
        model = User
        fields = '__all__'
