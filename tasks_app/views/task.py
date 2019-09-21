"""ViewSet'ы для модели Task."""

from rest_framework import viewsets

from tasks_app.models import Task
from tasks_app.serializers import TaskSerializer, TaskTableSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Task."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


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
