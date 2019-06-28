from datetime import datetime

from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from api.models import Employee

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

    def create(self, validated_data) -> Employee:
        age = int(relativedelta(now, validated_data['date_of_birth']).years)
        full_name = f'{validated_data["last_name"]} {validated_data["first_name"]}'
        if validated_data['middle_name'] is not None:
            full_name = f'{validated_data["last_name"]} {validated_data["first_name"]} {validated_data["middle_name"]}'
        instance: Employee = Employee.objects.create(age=age, full_name=full_name, **validated_data)

        return instance

    def update(self, instance: Employee, validated_data) -> Employee:
        age = int(relativedelta(now, validated_data['date_of_birth']).years)
        full_name = f'{validated_data["last_name"]} {validated_data["first_name"]}'
        if validated_data['middle_name'] is not None:
            full_name = f'{validated_data["last_name"]} {validated_data["first_name"]} {validated_data["middle_name"]}'

        validated_data['full_name'] = full_name
        validated_data['age'] = age

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance


class EmployeeTableSerializer(BaseEmployeeSerializer):
    """Сериалайзер модели Employee для отображения в таблице."""

    sex = serializers.SerializerMethodField()

    class Meta:
        model = BaseEmployeeSerializer.Meta.model
        fields = ('id', 'full_name', 'registration_date', 'phone', 'email', 'date_of_birth', 'age', 'sex')

    @staticmethod
    def get_sex(instance: Employee):
        if instance.sex == 'male':
            return 'Муж.'
        return 'Жен.'
