"""Сериалайзеры для модели Employee."""

from datetime import datetime

from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from rest_api.models import Avatar, Employee
from rest_api.serializers import AvatarSerializer
from rest_api.tasks import greetings_via_email

now = datetime.now()


class EmployeeSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер для модели Employee."""

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeNestedSerializer(EmployeeSerializer):
    """Сериалайзер для модели Employee."""

    age = serializers.IntegerField(read_only=True, required=False)
    avatar = AvatarSerializer(many=False, required=False)

    def create(self, validated_data: dict) -> Employee:
        """
        Переопределение метода бозового метода create.

        :param validated_data: провалидированные данные
        :return: созданный объект модели
        """
        age = int(relativedelta(now, validated_data['date_of_birth']).years)

        avatar_object = validated_data.pop('avatar', None)
        avatar = None
        if avatar_object is not None:
            avatar = Avatar.objects.create(**avatar_object)

        validated_data['age'] = age
        validated_data['avatar'] = avatar

        instance = Employee.objects.create(**validated_data)

        greetings_via_email.delay(instance.email, instance.first_name, instance.middle_name)

        return instance

    def update(self, instance: Employee, validated_data: dict) -> Employee:
        """
        Переопределение базового метода update.

        :param instance: моедль, которую нужно обновить
        :param validated_data: провалидированные данные
        :return: объект обновленной модели
        """
        date_of_birth = validated_data.get('date_of_birth', None)
        if date_of_birth is not None:
            age = int(relativedelta(now, validated_data['date_of_birth']).years)
            validated_data['age'] = age

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save(update_fields=validated_data.keys())

        return instance


class EmployeeTableSerializer(EmployeeSerializer):
    """Сериалайзер модели Employee для отображения в таблице."""

    avatar = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeSerializer.Meta.model
        fields = (
            'id', 'first_name', 'last_name', 'middle_name', 'registration_date', 'phone', 'email', 'date_of_birth',
            'age', 'sex', 'avatar')

    @staticmethod
    def get_avatar(instance: Employee) -> str or None:
        """
        Функция получения значения в поле avatar.

        :param instance: объект модели Employee
        :return: относительный путь до файла или None
        """
        if instance.avatar is not None:
            return instance.avatar.file.url
        return None
