"""Сериалайзеры для модели User."""

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from auth_api.models import User


class BaseUserSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер модели User."""

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data: dict) -> User:
        """
        Переопределение метда создания пользователя.

        :param validated_data: провалидированные данные
        :return: созданный объект
        """
        password = validated_data.pop('password', None)
        if password is None:
            raise serializers.ValidationError('Необходимо указать пароль')

        password_hash = make_password(password)

        instance = User.objects.create(password=password_hash, **validated_data)

        return instance
