from rest_framework import serializers
from api.models import Employee, Attachment
from api.serializers.attachment import BaseAttachmentSerializer

from dateutil.relativedelta import relativedelta
from datetime import datetime

now = datetime.now()


class BaseEmployeeSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер для модели Employee."""

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeSerializer(BaseEmployeeSerializer):
    """Сериалайзер для модели Employee."""

    attachment = BaseAttachmentSerializer(many=False, allow_null=True)
    age = serializers.IntegerField(read_only=True)

    def create(self, validated_data) -> Employee:
        age = int(relativedelta(now, validated_data['date_of_birth']).years)
        attachment: dict = validated_data.pop('attachment', None)
        if attachment is not None:
            attachment: Attachment = Attachment.objects.create(**attachment)
        instance: Employee = Employee.objects.create(age=age, attachment=attachment, **validated_data)

        return instance

    def update(self, instance: Employee, validated_data) -> Employee:
        age = int(relativedelta(now, validated_data['date_of_birth']).years)
        instance.__dict__.update(age=age, **validated_data)
        instance.save()

        return instance


class EmployeeTableSerializer(BaseEmployeeSerializer):
    """Сериалайзер модели Employee для отображения в таблице."""

    employee_fio = serializers.SerializerMethodField()
    sex = serializers.SerializerMethodField()

    class Meta:
        model = BaseEmployeeSerializer.Meta.model
        fields = ('id', 'employee_fio', 'registration_date', 'phone', 'email', 'date_of_birth', 'age', 'sex')

    @staticmethod
    def get_employee_fio(instance: Employee):
        if instance.middle_name is not None:
            return f'{instance.last_name} {instance.first_name} {instance.middle_name}'
        return f'{instance.last_name} {instance.first_name}'

    @staticmethod
    def get_sex(instance: Employee):
        if instance.sex == 'male':
            return 'Муж.'
        return 'Жен.'
