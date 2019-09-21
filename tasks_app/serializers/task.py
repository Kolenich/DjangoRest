"""Сериалайзеры модели Task."""

from rest_framework import serializers

from tasks_app.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер для модели Task."""

    class Meta:
        model = Task
        fields = '__all__'


class TaskTableSerializer(TaskSerializer):
    """Табличное представление для модели Task."""

    assigned_by = serializers.SerializerMethodField()
    assigned_to = serializers.SerializerMethodField()

    @staticmethod
    def get_assigned_by(instance: Task) -> str:
        """
        Метод для получения имени и фамили того, кто назначили задание.

        :param instance: объект модели Task
        :return: имя и фамилия назначившего
        """
        return f'{instance.assigned_by.last_name} {instance.assigned_by.first_name}'

    @staticmethod
    def get_assigned_to(instance: Task) -> str:
        """
        Метод для получения имени и фамили того, кому назначили задание.

        :param instance: объект модели Task
        :return: имя и фамилия назначенного
        """
        return f'{instance.assigned_to.last_name} {instance.assigned_to.first_name}'
