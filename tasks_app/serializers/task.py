"""Сериалайзеры модели Task."""

from rest_framework import serializers
from rest_framework.request import Request

from tasks_app.models import Task
from tasks_app.tasks import task_assigned_notification
from users_app.models import User
from users_app.serializers import UserTaskDetailSerializer


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

    assigned_by = UserTaskDetailSerializer(many=False, required=False)

    class Meta(TaskMeta):
        fields = None
        exclude = ('assigned_to',)


class AssignedTaskSerializer(TaskSerializer):
    """Сериалайзер модели Task для назначения задачи."""

    assigned_by = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    def create(self, validated_data: dict) -> Task:
        """
        Переопределение метода создания задачи.

        :param validated_data:
        :return: объект созданной задачи
        """
        request: Request = self.context['request']

        validated_data['assigned_by_id'] = request.user.id

        instance = Task.objects.create(**validated_data)

        assigned_to_user: User = validated_data['assigned_to']

        email = User.objects.get(pk=assigned_to_user.pk).email
        task = {
            'summary': validated_data['summary'],
            'description': validated_data['description'],
            'dead_line': validated_data['dead_line'].strftime('%d.%m.%Y'),
            'comment': validated_data['comment'],
        }
        assigned_by = f'{request.user.last_name} {request.user.first_name}'

        task_assigned_notification.delay(email, task, assigned_by)

        return instance


class TaskTableSerializer(TaskSerializer):
    """Табличное представление для модели Task."""

    assigned_by = serializers.SerializerMethodField()

    class Meta(TaskMeta):
        fields = None
        exclude = ('done',)

    @staticmethod
    def get_assigned_by(instance: Task) -> str:
        """
        Метод для получения имени и фамили того, кто назначили задание.

        :param instance: объект модели Task
        :return: имя и фамилия назначившего
        """
        return f'{instance.assigned_by.last_name} {instance.assigned_by.first_name}'
