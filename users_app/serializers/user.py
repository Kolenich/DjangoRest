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

    first_name = serializers.SlugRelatedField(source='user', slug_field='first_name', read_only=True)
    last_name = serializers.SlugRelatedField(source='user', slug_field='last_name', read_only=True)

    class Meta(ProfileMeta):
        fields = ('first_name', 'last_name')


class ProfileDetailSerializer(ProfileSerializer):
    """Сериалайзер модели Profile для отображения в угловом меню."""

    first_name = serializers.SlugRelatedField(source='user', slug_field='first_name', read_only=True)
    last_name = serializers.SlugRelatedField(source='user', slug_field='last_name', read_only=True)
    email = serializers.SlugRelatedField(source='user', slug_field='email', read_only=True)

    class Meta(ProfileMeta):
        fields = ('first_name', 'last_name', 'email')


class ProfileAssignmentSerializer(ProfileSerializer):
    """Представление модели User для фльтрации в таблице задач."""

    value = serializers.SlugRelatedField(source='user', slug_field='pk', read_only=True)
    label = serializers.SerializerMethodField(method_name='select_label')
    key = serializers.SlugRelatedField(source='user', slug_field='pk', read_only=True)

    class Meta(ProfileMeta):
        fields = ('key', 'value', 'label')

    @staticmethod
    def select_label(instance: Profile) -> str:
        """
        Метод для получения ярлыка для селекта фильтрации в таблице задач.

        :param instance: объект модели User
        :return: имя и фамилия пользователя
        """
        return f'{instance.user.last_name} {instance.user.first_name}'
