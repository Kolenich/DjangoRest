from rest_framework import serializers
from api.models import Organization
from api.serializers import EmployeeSerializer


class BaseOrganisationSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер для модели Organization."""

    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationSerializer(BaseOrganisationSerializer):
    """Сериалайзер для модели Organization."""

    employees = EmployeeSerializer(many=True, required=False)
