"""ViewSet'ы для модели Task."""

from rest_framework.request import Request
from rest_framework.response import Response

from tasks_app.models import Task
from tasks_app.serializers import TaskSerializer, TaskTableSerializer
from tools import CustomListMixin


class TaskViewSet(CustomListMixin):
    """ViewSet для модели Task."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request: Request, *args, **kwargs) -> Response:
        """
        Переопределние метода выдачи списка заданий.

        Возвращает только те задания, которые назначены зарегистрированному пользователю.

        :param request: объект запроса
        :param args: дополнительные параметры списом
        :param kwargs: дополнительные параметры словарем
        :return: отфильтрованный кверисет
        """
        user_id = request.user.id

        queryset = Task.objects.filter(assigned_to_id=user_id)

        response = self.custom_list(queryset)

        return response


class TaskTableViewset(TaskViewSet):
    """Табличное представление всех задач."""

    serializer_class = TaskTableSerializer

    filterset_fields = {
        'summary': ('icontains', 'istartswith', 'iendswith', 'exact',),
        'description': ('icontains', 'istartswith', 'iendswith', 'exact'),
        'comment': ('icontains', 'istartswith', 'iendswith', 'exact'),
        'date_of_issue': ('gte', 'gt', 'lte', 'lt', 'exact'),
        'dead_line': ('gte', 'gt', 'lte', 'lt', 'exact'),
        'done': ('exact',),
        'assigned_by_id': ('exact',),
        'assigned_to_id': ('exact',),
    }
    ordering_fields = '__all__'
