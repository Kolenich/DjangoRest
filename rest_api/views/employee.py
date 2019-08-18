"""ViewSet'ы для модели Employee."""

from rest_framework import viewsets

from rest_api.models import Employee
from rest_api.serializers import EmployeeNestedSerializer, EmployeeTableSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Employee."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeNestedSerializer


class EmployeeTableViewSet(EmployeeViewSet):
    """ViewSet модели Employee для отображения в таблице."""

    serializer_class = EmployeeTableSerializer
    filterset_fields = {
        'phone': ('icontains', 'istartswith', 'iendswith', 'exact',),
        'email': ('icontains', 'istartswith', 'iendswith', 'exact'),
        'age': ('gte', 'gt', 'lte', 'lt', 'exact'),
        'first_name': ('icontains', 'istartswith', 'iendswith', 'exact'),
        'last_name': ('icontains', 'istartswith', 'iendswith', 'exact'),
        'middle_name': ('icontains', 'istartswith', 'iendswith', 'exact'),
        'sex': ('exact',),
        'registration_date': ('gte', 'gt', 'lte', 'lt'),
        'date_of_birth': ('gte', 'gt', 'lte', 'lt', 'exact'),
    }
    ordering_fields = (
        'phone', 'email', 'age', 'first_name', 'last_name', 'middle_name', 'sex', 'registration_date', 'date_of_birth')
