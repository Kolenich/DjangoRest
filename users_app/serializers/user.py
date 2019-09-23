"""Сериалайзеры для модели User."""

from rest_framework import serializers

from users_app.models import User


class UserMeta:
    """Базовый мета-класс для сериалайзеров модели User."""

    model = User
    fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер модели User."""

    class Meta(UserMeta):
        pass


class UserTaskDetailSerializer(UserSerializer):
    """Сериалайзер модели User для отображения в подробностях задания."""

    class Meta(UserMeta):
        fields = ('first_name', 'last_name')


class UserProfileSerializer(UserSerializer):
    """Сериалайзер модели User для отображения в угловом меню."""

    class Meta(UserMeta):
        fields = ('first_name', 'last_name', 'email')


class UserAssignmentSerializer(UserSerializer):
    """Представление модели User для фльтрации в таблице задач."""

    value = serializers.SerializerMethodField(method_name='select_value')
    label = serializers.SerializerMethodField(method_name='select_label')
    key = serializers.SerializerMethodField(method_name='select_key')

    class Meta(UserMeta):
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
    def select_label(instance: User) -> str:
        """
        Метод для получения ярлыка для селекта фильтрации в таблице задач.

        :param instance: объект модели User
        :return: имя и фамилия пользователя
        """
        return f'{instance.last_name} {instance.first_name}'

    @staticmethod
    def select_key(instance: User) -> int:
        """
         Метод для получения ключа для селекта фильтрации в таблице задач.

        :param instance: объект модели User
        :return: первичный ключ модели
        """
        return instance.id
