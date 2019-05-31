from rest_framework import serializers
from api.models import Organization
from api.serializers import EmployeeSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели Organization
    """
    employees = EmployeeSerializer(many=True, required=False)

    class Meta:
        model = Organization
        fields = '__all__'
