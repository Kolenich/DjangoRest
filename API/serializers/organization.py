from rest_framework import serializers
from API.models import Organization, Employee
from API.serializers import EmployeeSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели Organization
    """
    employees = EmployeeSerializer(many=True, required=False)

    class Meta:
        model = Organization
        fields = '__all__'

    def create(self, validated_data):
        employees: list = validated_data.pop('employees', [])
        instance: Organization = Organization.objects.create(**validated_data)

        for employee in employees:
            Employee.objects.create(organization=instance, **employee)

        return instance

    def update(self, instance: Organization, validated_data):
        employees: list = validated_data.pop('employees', [])
        instance.__dict__.update(**validated_data)

        valid_employees: list = []
        for item in employees:
            try:
                employee: Employee = Employee.objects.get(id=item['id'])
                employee.__dict__.update(**item)
                valid_employees.append(employee)
            except KeyError:
                employee: Employee = Employee.objects.create(organization=instance, **item)
                valid_employees.append(employee)
        for employee in valid_employees:
            employee.save()

        instance.save()

        return instance
