"""Сериалайзеры модели Avatar."""

from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from rest_api.models import Avatar


class AvatarSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер для модели Avatar."""

    file = Base64ImageField()

    class Meta:
        model = Avatar
        fields = '__all__'
