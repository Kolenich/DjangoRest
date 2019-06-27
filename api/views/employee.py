from rest_framework import viewsets

from api.models import Employee
from api.serializers import EmployeeSerializer, EmployeeTableSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Employee."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeTableViewSet(EmployeeViewSet):
    """ViewSet модели Employee для отображения в таблице."""

    serializer_class = EmployeeTableSerializer
    filterset_fields = {
        'id': ('contains',),
        'phone': ('contains',),
        'email': ('contains',),
        'age': ('contains',),
        'full_name': ('contains',),
        'sex': ('startswith',),
        'registration_date': ('gte', 'lte'),
        'date_of_birth': ('gte', 'lte'),
    }
    ordering_fields = ('id', 'phone', 'email', 'age', 'full_name', 'sex', 'registration_date', 'date_of_birth')
