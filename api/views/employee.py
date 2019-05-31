from rest_framework import viewsets
from api.models import Employee
from api.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Customer
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
