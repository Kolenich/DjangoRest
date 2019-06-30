"""ViewSet'ы для модели Employee."""

from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from api.models import Employee, Avatar
from api.serializers import EmployeeSerializer, EmployeeTableSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Employee."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def destroy(self, request: Request, pk=None, *args, **kwargs) -> Response:
        """
        Переопределение базового метода destroy.

        :param request: объект запроса
        :param pk: первичный ключ удаляемогообъекта
        :param args: дополнительные аргументы массива
        :param kwargs: дополнительные аргументы словаря
        :return: ответ со статусом 204 об успешном удалении или 500
        """
        try:
            employee: Employee = Employee.objects.get(pk=pk)
            try:
                avatar: Avatar = Avatar.objects.get(pk=employee.avatar_id)
                avatar.delete()
            except Avatar.DoesNotExist:
                pass
            employee.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Employee.DoesNotExist:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeTableViewSet(EmployeeViewSet):
    """ViewSet модели Employee для отображения в таблице."""

    serializer_class = EmployeeTableSerializer
    filterset_fields = {
        'phone': ('contains',),
        'email': ('contains',),
        'age': ('contains',),
        'full_name': ('contains',),
        'sex': ('startswith',),
        'registration_date': ('gte', 'lte'),
        'date_of_birth': ('gte', 'lte'),
    }
    ordering_fields = ('phone', 'email', 'age', 'full_name', 'sex', 'registration_date', 'date_of_birth')
