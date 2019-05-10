from rest_framework import serializers
from API.models import Employee
from API.serializers.attachment import AttachmentSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели Employee
    """
    id = serializers.IntegerField(required=False)
    attachment = AttachmentSerializer(many=False)

    class Meta:
        model = Employee
        fields = '__all__'
