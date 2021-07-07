"""Сериалайзеры модели Task."""

from rest_framework import serializers

from common_models.serializers import AttachmentSerializer
from tasks.models import Task
from tasks.tools import send_email
from users.serializers import UserTaskDetailSerializer


class TaskSerializer(serializers.ModelSerializer):
    """Основной сериалайзер для модели Task."""

    assigned_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']
        validated_data['assigned_by'] = request.user
        instance = self.Meta.model.objects.create(**validated_data)
        if instance.assigned_to.profile.mailing:
            send_email(
                f'Пользователь {request.user.username} назначил Вам задание',
                instance.email_template,
                [instance.assigned_to.email],
                verbose_name='Отправка почты',
                creator=request.user
            )
        instance.to_websocket()
        return instance


class TaskDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Task для отображения деталей задания."""

    assigned_by = UserTaskDetailSerializer(read_only=True)
    attachment = AttachmentSerializer(read_only=True)

    class Meta:
        model = Task
        exclude = ('assigned_to',)


class TaskDashboardSerializer(serializers.ModelSerializer):
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
        return f'{instance.assigned_by.last_name} {instance.assigned_by.first_name}'
