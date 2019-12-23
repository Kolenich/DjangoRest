"""Файл с viewset'ами для модели User."""

from django.db.utils import IntegrityError
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from mixins import ModelViewSet
from users_app.models import User
from users_app.serializers import UserAssignmentSerializer, UserProfileSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    """Базовый viewset для модели Пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(UserViewSet):
    """ViewSet для выгрущки данных о пользователе в уголовое меню."""

    queryset = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)
    serializer_class = UserProfileSerializer

    @action(methods=['get'], detail=False)
    def user(self, request: Request):
        """
        Метод для получения данных о конкретном юзере.

        :param request: объект запроса
        :return: объект ответа с данными о юзере
        """
        try:
            user = self.get_queryset().get(email=request.user.email)

            serializer = self.get_serializer(user)

            return Response(serializer.data, HTTP_200_OK)
        except User.DoesNotExist:
            data = {'message': 'Указанный пользователь не найден'}

            return Response(data, HTTP_404_NOT_FOUND)


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
        queryset = self.get_queryset().exclude(id=request.user.id)

        response = self.get_paginated_list(queryset)

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

        try:
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
        except KeyError:
            return response

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
