"""Сериалайзеры для модели User."""

from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Сериалайзер профиля."""

    class Meta:
        model = Profile
        exclude = ('user',)


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер модели User."""

    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ('password',)


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
