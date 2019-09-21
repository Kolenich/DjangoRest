"""Файл с viewset'ами для модели User."""

from django.db.utils import IntegrityError
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from auth_api.models import User
from auth_api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Базовый viewset для модели Пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


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
            User.objects.create_user(**request.data)
            data['message'] = 'Пользователь создан успешно'
            response = Response(data, HTTP_201_CREATED)
        except IntegrityError:
            data['message'] = 'Пользователь с данной почтой уже существует'
            data['errors'] = ('email',)
            response = Response(data, HTTP_400_BAD_REQUEST)
        except ValueError:
            data['message'] = 'Необходимо указать электронную почту'
            data['errors'] = ('email',)
            response = Response(data, HTTP_400_BAD_REQUEST)

        return response
