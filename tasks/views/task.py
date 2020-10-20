"""ViewSet'ы для модели Task."""

from django.db import transaction
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR

from common_models.models import Attachment
from tasks.models import Task
from tasks.serializers import TaskDetailSerializer, TaskSerializer, TaskDashboardSerializer
from tasks.tasks import task_assigned_notification


class TaskDashboardViewSet(viewsets.ModelViewSet):
    """Представление для Task на главной странице."""

    filterset_fields = {
        'summary': ('icontains', 'istartswith', 'iendswith', 'exact', 'ne'),
        'description': ('icontains', 'istartswith', 'iendswith', 'exact', 'ne'),
        'comment': ('icontains', 'istartswith', 'iendswith', 'exact', 'ne'),
        'date_of_issue': ('gte', 'gt', 'lte', 'lt', 'ne'),
        'dead_line': ('gte', 'gt', 'lte', 'lt', 'ne'),
        'done': ('exact', 'ne'),
        'assigned_by_id': ('exact',),
        'assigned_to_id': ('exact',),
    }

    ordering_fields = ('summary', 'description', 'comment', 'date_of_issue', 'dead_line', 'assigned_by__last_name')

    serializer_class = TaskDashboardSerializer

    def get_queryset(self):
        # Возвращаем только те задания, которые назначены на пользователя
        return Task.objects.filter(assigned_to=self.request.user, archived=False)


class TaskViewSet(viewsets.ModelViewSet):
    """Базовый viewset для модели Tasks."""

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskDetailSerializer
        return TaskSerializer

    def get_queryset(self):
        # Возвращаем только те задания, к которым пользователь имеет отношение
        user_criteria = Q(assigned_to=self.request.user) | Q(assigned_by=self.request.user)
        return Task.objects.filter(user_criteria, archived=False)

    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        user_criteria = Q(assigned_to=self.request.user) | Q(assigned_by=self.request.user)
        # Возвращаем только те задания, к которым пользователь имеет отношение
        if task.assigned_to != self.request.user and task.assigned_by != self.request.user:
            return Response({'detail': 'Вы не имеете доступ к этому заданию'}, HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(task)
        print(serializer.data)
        return Response(serializer.data, HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='attach-file')
    @transaction.atomic
    def attach_file(self, request, *args, **kwargs):
        """Экшн для прикладывания файла к заданию."""
        data = {'detail': 'Некорректный запрос'}
        status = HTTP_400_BAD_REQUEST

        task = self.get_object()

        try:
            attachment = {
                'file': request.data.get('file'),
                'file_name': request.data.get('file_name'),
                'file_mime': request.data.get('file_mime'),
                'file_size': int(request.data.get('file_size'))
            }
            task.attachment = Attachment.objects.create(**attachment)
            task.save()

            # Если пользователь при регистрации поставил галочку "Рассылка на почту", то отправляем письмо
            if task.assigned_to.profile.mailing:
                task_object = {
                    'summary': task.summary,
                    'description': task.description,
                    'dead_line': task.dead_line.strftime('%d.%m.%Y'),
                    'comment': task.comment,
                }
                assigned_by = f'{request.user.last_name} {request.user.first_name}'

                task_assigned_notification.delay(task.assigned_to.user.email, task_object, assigned_by)

            data = self.get_serializer(task).data
            status = HTTP_200_OK
        except Exception as exc:
            task.delete()
            data['detail'] = f'При создании произошла ошибка: {str(exc)}'
            status = HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data, status)
