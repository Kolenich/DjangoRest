"""ViewSet'ы для модели Task."""

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR

from common_models_app.models import Attachment
from mixins import ModelViewSet
from tasks_app.models import Task
from tasks_app.serializers import AssignedTaskSerializer, TaskDetailSerializer, TaskSerializer, TaskTableSerializer
from tasks_app.tasks import task_assigned_notification


class TaskViewSet(ModelViewSet):
    """Базовый viewset для модели Tasks."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailViewSet(TaskViewSet):
    """ViewSet модели Task для отображения деталей задания."""

    serializer_class = TaskDetailSerializer

    def retrieve(self, request: Request, *args, **kwargs):
        """
        Переопределение метода выдачи одной записи в БД.

        :param request: объект запроса
        :param args: параметры массива
        :param kwargs: параметры словаря
        :return: 200 и найденный объект, 404 и сообщение об отсутствии или 403
        """
        instance = self.get_object()
        # Достаем все задачи, которые есть у пользователя
        user_tasks = request.user.tasks_taken.all()
        # Если запрашиваемая задача есть у пользователя, возвращаем её
        if instance in user_tasks:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        # Иначе возвращаем 403
        else:
            data = {'message': 'У вас нет доступа к этому заданию'}
            return Response(data, HTTP_403_FORBIDDEN)


class AssignedTaskViewSet(TaskViewSet):
    """ViewSet для сохранения задач в БД."""

    serializer_class = AssignedTaskSerializer

    @action(methods=['post'], detail=True, url_path='attach-file')
    def attach_file(self, request: Request, pk=None) -> Response:
        """Экшн для прикладывания файла к заданию."""
        data = {'message': 'Некорректный запрос'}
        status = HTTP_400_BAD_REQUEST

        task = self.get_queryset().get(pk=pk)

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
            if task.assigned_to.mailing:
                task_object = {
                    'summary': task.summary,
                    'description': task.description,
                    'dead_line': task.dead_line.strftime('%d.%m.%Y'),
                    'comment': task.comment,
                }
                assigned_by = f'{request.user.last_name} {request.user.first_name}'

                task_assigned_notification.delay(task.assigned_to.email, task_object, assigned_by)

            data = self.get_serializer(task).data
            status = HTTP_200_OK
        except Exception as exc:
            task.delete()
            data['message'] = f'При создании произошла ошибка: {str(exc)}'
            status = HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data, status)


class TaskTableViewset(TaskViewSet):
    """Табличное представление всех задач."""

    serializer_class = TaskTableSerializer

    filterset_fields = {
        'summary': ('icontains', 'istartswith', 'iendswith', 'exact',),
        'description': ('icontains', 'istartswith', 'iendswith', 'exact'),
        'comment': ('icontains', 'istartswith', 'iendswith', 'exact'),
        'date_of_issue': ('gte', 'gt', 'lte', 'lt'),
        'dead_line': ('gte', 'gt', 'lte', 'lt'),
        'done': ('exact',),
        'assigned_by_id': ('exact',),
        'assigned_to_id': ('exact',),
    }
    ordering_fields = ('summary', 'description', 'comment', 'date_of_issue', 'dead_line', 'assigned_by__last_name')

    def list(self, request: Request, *args, **kwargs) -> Response:
        """
        Переопределние метода выдачи списка заданий.

        Возвращает только те задания, которые назначены зарегистрированному пользователю.

        :param request: объект запроса
        :param args: дополнительные параметры списом
        :param kwargs: дополнительные параметры словарем
        :return: отфильтрованный кверисет
        """
        queryset = self.get_queryset().filter(assigned_to=request.user, archived=False)

        response = self.get_paginated_list(queryset)

        return response
