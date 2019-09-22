"""Файл с viewset'ами для модели User."""

from django.db.utils import IntegrityError
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from tools import CustomModelViewSet
from users_app.models import User
from users_app.serializers import UserAssignmentSerializer, UserSerializer


class UserViewSet(CustomModelViewSet):
    """Базовый viewset для модели Пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAssignmentViewset(UserViewSet):
    """Viewset для выгрузки всех юзеров для отображения в строке фильтрации для таблицы задач."""

    queryset = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)
    serializer_class = UserAssignmentSerializer

    def list(self, request: Request, *args, **kwargs) -> Response:
        """
        Переопределение метода выдачи пользователей для фильтрации по заказчику.

        Ислючает из списка пользователя, сделавшего запрос.

        :param request: объект запроса
        :param args: дополнительные параметры списом
        :param kwargs: дополнительные параметры словарем
        :return: отфильтрованный кверисет
        """
        user_id = request.user.id

        queryset = self.get_queryset().exclude(id=user_id)

        response = self.custom_list(queryset)

        return response


class UserRegistrationViewSet(UserViewSet):
    """Класс для регистрации пользователей."""

    permission_classes = (AllowAny,)

    @action(methods=['post'], detail=False)
    def registrate(self, request: Request) -> Response:
        """
        Экшн для регистрации новых пользователей.

        :param request: объект запроса
        :return: 201 или 400
        """
        data = {'message': 'Неверные данные'}
        response = Response(data, HTTP_400_BAD_REQUEST)

        if request.data['first_name'] == '':
            data['message'] = 'Имя не может быть пустым'
            data['errors'] = {'first_name': True}
            return Response(data, HTTP_400_BAD_REQUEST)

        if request.data['last_name'] == '':
            data['message'] = 'Фамилия не может быть пустой'
            data['errors'] = {'last_name': True}
            return Response(data, HTTP_400_BAD_REQUEST)

        if request.data['password'] == '':
            data['message'] = 'Необходимо указать пароль'
            data['errors'] = {'password': True}
            return Response(data, HTTP_400_BAD_REQUEST)

        try:
            User.objects.create_user(**request.data)
            data['message'] = 'Пользователь создан успешно'
            response = Response(data, HTTP_201_CREATED)
        except IntegrityError:
            data['message'] = 'Пользователь с данной почтой уже существует'
            data['errors'] = {'email': True}
            response = Response(data, HTTP_400_BAD_REQUEST)
        except ValueError:
            data['message'] = 'Необходимо указать электронную почту'
            data['errors'] = {'email': True}
            response = Response(data, HTTP_400_BAD_REQUEST)

        return response
