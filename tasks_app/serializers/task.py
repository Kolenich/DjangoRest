"""Сериалайзеры модели Task."""

from rest_framework import serializers

from common_models_app.serializers import AttachmentSerializer
from tasks_app.models import Task
from users_app.serializers import ProfileTaskDetailSerializer


class TaskSerializer(serializers.ModelSerializer):
    """Основной сериалайзер для модели Task."""

    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Task для отображения деталей задания."""

    assigned_by = ProfileTaskDetailSerializer(read_only=True)
    attachment = AttachmentSerializer(read_only=True)

    class Meta:
        model = Task
        exclude = ('assigned_to',)


class TaskTableSerializer(serializers.ModelSerializer):
    """Табличное представление для модели Task."""

    assigned_by = serializers.SerializerMethodField()
    attachment = AttachmentSerializer(read_only=True)

    class Meta:
        model = Task
        exclude = ('done',)

    @staticmethod
    def get_assigned_by(instance: Task) -> str:
        """
        Метод для получения имени и фамили того, кто назначили задание.

        :param instance: объект модели Task
        :return: имя и фамилия назначившего
        """
        return f'{instance.assigned_by.user.last_name} {instance.assigned_by.user.first_name}'
