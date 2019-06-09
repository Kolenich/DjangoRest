from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from auth_api.models import User


class BaseUserSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер модели User."""

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data) -> User:
        """Переопределение метда создания пользователя."""

        password: str = validated_data.pop('password', None)
        if password is None:
            raise serializers.ValidationError('Необходимо указать пароль')

        password_hash: str = make_password(password)

        instance: User = User.objects.create(password=password_hash, **validated_data)

        return instance
