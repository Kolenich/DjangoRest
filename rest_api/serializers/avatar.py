"""Сериалайзеры модели Avatar."""

from rest_framework import serializers

from rest_api.models import Avatar


class AvatarSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер для модели Avatar."""

    class Meta:
        model = Avatar
        fields = '__all__'
