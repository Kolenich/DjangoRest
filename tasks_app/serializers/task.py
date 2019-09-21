"""Сериалайзеры модели Task."""

from rest_framework import serializers

from tasks_app.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер для модели Task."""

    class Meta:
        model = Task
        fields = '__all__'
