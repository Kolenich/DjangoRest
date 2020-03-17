"""Сериалайзеры для модели User."""

from rest_framework import serializers

from users_app.models import Profile


class ProfileMeta:
    """Базовый мета-класс для сериалайзеров модели Profile."""

    model = Profile
    fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер модели Profile."""

    class Meta(ProfileMeta):
        pass


class ProfileTaskDetailSerializer(ProfileSerializer):
    """Сериалайзер модели Profile для отображения в подробностях задания."""

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    @staticmethod
    def get_first_name(instance: Profile):
        """Метод для получения имени пользователя."""
        return instance.user.first_name

    @staticmethod
    def get_last_name(instance: Profile):
        """Метод для получения фамилии пользователя."""
        return instance.user.last_name

    class Meta(ProfileMeta):
        fields = ('first_name', 'last_name')


class ProfileDetailSerializer(ProfileSerializer):
    """Сериалайзер модели Profile для отображения в угловом меню."""

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    @staticmethod
    def get_first_name(instance: Profile):
        """Метод для получения имени пользователя."""
        return instance.user.first_name

    @staticmethod
    def get_last_name(instance: Profile):
        """Метод для получения фамилии пользователя."""
        return instance.user.last_name

    @staticmethod
    def get_email(instance: Profile):
        """Метод для получения фамилии пользователя."""
        return instance.user.email

    class Meta(ProfileMeta):
        fields = ('first_name', 'last_name', 'email')


class ProfileAssignmentSerializer(ProfileSerializer):
    """Представление модели User для фльтрации в таблице задач."""

    value = serializers.SerializerMethodField(method_name='select_value')
    label = serializers.SerializerMethodField(method_name='select_label')
    key = serializers.SerializerMethodField(method_name='select_key')

    class Meta(ProfileMeta):
        fields = ('key', 'value', 'label')

    @staticmethod
    def select_value(instance: Profile) -> int:
        """
        Метод для получения значения для селекта фильтрации в таблице задач.

        :param instance: объект модели User
        :return: первичный ключ модели
        """
        return instance.user.pk

    @staticmethod
    def select_label(instance: Profile) -> str:
        """
        Метод для получения ярлыка для селекта фильтрации в таблице задач.

        :param instance: объект модели User
        :return: имя и фамилия пользователя
        """
        return f'{instance.user.last_name} {instance.user.first_name}'

    @staticmethod
    def select_key(instance: Profile) -> int:
        """
         Метод для получения ключа для селекта фильтрации в таблице задач.

        :param instance: объект модели User
        :return: первичный ключ модели
        """
        return instance.user.pk
