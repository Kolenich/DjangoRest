"""Сериалайзеры для модели User."""

from rest_framework import serializers

from users_app.models import User


class UserSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер модели User."""

    class Meta:
        model = User
        fields = '__all__'


class UserAssignmentSerializer(UserSerializer):
    """Представление модели User для фльтрации в таблице задач."""

    value = serializers.SerializerMethodField(method_name='select_value')
    label = serializers.SerializerMethodField()
    key = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('key', 'value', 'label')

    @staticmethod
    def select_value(instance: User) -> int:
        """
        Метод для получения значения для селекта фильтрации в таблице задач.

        :param instance: объект модели User
        :return: первичный ключ модели
        """
        return instance.id

    @staticmethod
    def get_label(instance: User) -> str:
        """
        Метод для получения ярлыка для селекта фильтрации в таблице задач.

        :param instance: объект модели User
        :return: имя и фамилия пользователя
        """
        return f'{instance.last_name} {instance.first_name}'

    @staticmethod
    def get_key(instance: User) -> int:
        """
         Метод для получения ключа для селекта фильтрации в таблице задач.

        :param instance: объект модели User
        :return: первичный ключ модели
        """
        return instance.id
