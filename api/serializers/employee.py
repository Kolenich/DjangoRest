"""Сериалайзеры для модели Employee."""

from datetime import datetime

from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from api.models import Employee, Avatar
from api.serializers import BaseAvatarSerializer

now = datetime.now()


class BaseEmployeeSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер для модели Employee."""

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeSerializer(BaseEmployeeSerializer):
    """Сериалайзер для модели Employee."""

    age = serializers.IntegerField(read_only=True, required=False)
    full_name = serializers.CharField(read_only=True, required=False)
    avatar = BaseAvatarSerializer(many=False, allow_null=True)

    def create(self, validated_data) -> Employee:
        """
        Переопределение метода бозового метода create.

        :param validated_data: провалидированные данные
        :return: созданный объект модели
        """
        age = int(relativedelta(now, validated_data['date_of_birth']).years)

        full_name = f'{validated_data["last_name"]} {validated_data["first_name"]}'
        if validated_data['middle_name'] is not None:
            full_name = f'{validated_data["last_name"]} {validated_data["first_name"]} {validated_data["middle_name"]}'

        avatar = validated_data.pop('avatar', None)
        if avatar is not None:
            avatar = Avatar.objects.create(**avatar)

        instance: Employee = Employee.objects.create(age=age, full_name=full_name, avatar=avatar, **validated_data)

        return instance

    def update(self, instance: Employee, validated_data) -> Employee:
        """
        Переопределение базового метода update.

        :param instance: моедль, которую нужно обновить
        :param validated_data: провалидированные данные
        :return: объект обновленной модели
        """
        age: int = int(relativedelta(now, validated_data['date_of_birth']).years)

        full_name = f'{validated_data["last_name"]} {validated_data["first_name"]}'
        if validated_data['middle_name'] is not None:
            full_name = f'{validated_data["last_name"]} {validated_data["first_name"]} {validated_data["middle_name"]}'

        # Удаляем старый аватар, если имеется
        current_avatar: Avatar = instance.avatar
        if current_avatar is not None:
            current_avatar.delete()

        avatar: dict = validated_data.pop('avatar', None)

        # Создаём новый аватар
        if avatar is not None:
            avatar: Avatar = Avatar.objects.create(**avatar)

        validated_data['full_name'] = full_name
        validated_data['age'] = age
        validated_data['avatar'] = avatar

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance


class EmployeeTableSerializer(BaseEmployeeSerializer):
    """Сериалайзер модели Employee для отображения в таблице."""

    sex = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = BaseEmployeeSerializer.Meta.model
        fields = ('id', 'full_name', 'registration_date', 'phone', 'email', 'date_of_birth', 'age', 'sex', 'avatar')

    @staticmethod
    def get_sex(instance: Employee):
        """
        Функция получения значения в поле sex.

        :param instance: объект модели Employee
        :return: Муж. или Жен.
        """
        if instance.sex == 'male':
            return 'Муж.'
        return 'Жен.'

    @staticmethod
    def get_avatar(instance: Employee):
        """
        Функция получения значения в поле avatar.

        :param instance: объект модели Employee
        :return: относительный путь до файла или None
        """
        if instance.avatar is not None:
            return instance.avatar.file.url
        return None
