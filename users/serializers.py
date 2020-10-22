"""Сериалайзеры для модели User."""

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Profile."""

    class Meta:
        model = User
        fields = '__all__'


class UserTaskDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер модели User для отображения в подробностях задания."""

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Profile для отображения в угловом меню."""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserAssignmentSerializer(serializers.ModelSerializer):
    """Представление модели User для фльтрации в таблице задач."""

    class Meta:
        model = User
        fields = ('pk', 'last_name', 'first_name')
