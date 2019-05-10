from rest_framework import serializers
from API.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели Employee
    """
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Employee
        fields = '__all__'
