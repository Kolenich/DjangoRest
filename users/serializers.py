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

    value = serializers.SerializerMethodField(method_name='user_value')
    label = serializers.SerializerMethodField()
    key = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('value', 'label', 'key')

    @staticmethod
    def get_label(instance):
        """
        Метод для получения ярлыка для селекта фильтрации в таблице задач.

        :param instance: объект модели User
        :return: имя и фамилия пользователя
        """
        return f'{instance.last_name} {instance.first_name}'

    @staticmethod
    def get_key(instance):
        return instance.pk

    @staticmethod
    def user_value(instance):
        return instance.pk
