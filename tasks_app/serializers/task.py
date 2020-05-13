"""Сериалайзеры модели Task."""

from rest_framework import serializers

from common_models_app.serializers import AttachmentSerializer
from tasks_app.models import Task
from users_app.serializers import ProfileTaskDetailSerializer


class TaskMeta:
    """Базовый мета-класс для сериалайзеров модели Task."""

    model = Task
    fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер для модели Task."""

    class Meta(TaskMeta):
        pass


class TaskDetailSerializer(TaskSerializer):
    """Сериалайзер модели Task для отображения деталей задания."""

    assigned_by = ProfileTaskDetailSerializer(many=False, read_only=True)
    attachment = AttachmentSerializer(many=False, read_only=True)

    class Meta(TaskMeta):
        fields = None
        exclude = ['assigned_to']


class TaskTableSerializer(TaskSerializer):
    """Табличное представление для модели Task."""

    assigned_by = serializers.SerializerMethodField()
    attachment = AttachmentSerializer(many=False, read_only=True)

    class Meta(TaskMeta):
        fields = None
        exclude = ['done']

    @staticmethod
    def get_assigned_by(instance: Task) -> str:
        """
        Метод для получения имени и фамили того, кто назначили задание.

        :param instance: объект модели Task
        :return: имя и фамилия назначившего
        """
        return f'{instance.assigned_by.user.last_name} {instance.assigned_by.user.first_name}'
