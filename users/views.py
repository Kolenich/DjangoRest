"""Файл с viewset'ами для модели User."""

from django.contrib.auth.models import User
from django.db import transaction
from django.db.utils import IntegrityError
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from users.models import Profile
from users.serializers import UserAssignmentSerializer, UserDetailSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Базовый viewset для модели Пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    @transaction.atomic
    def registrate(self, request):
        """
        Экшн для регистрации новых пользователей.

        :param request: объект запроса
        :return: 201 или 400
        """
        data = {'detail': 'Неверные данные'}

        user_data = {
            'first_name': request.data.pop('first_name', None),
            'last_name': request.data.pop('last_name', None),
            'password': request.data.pop('password', None),
            'email': request.data.pop('email', None),
            'username': request.data.pop('username', None),
        }

        profile_data = {
            'mailing': request.data.pop('mailing', False),
            'middle_name': request.data.pop('middle_name', None),
            'user': User.objects.create_user(**user_data)
        }

        try:
            if not user_data['first_name']:
                data['detail'] = 'Имя не может быть пустым'
                data['errors'] = {'first_name': True}
                return Response(data, HTTP_400_BAD_REQUEST)

            if not user_data['last_name']:
                data['detail'] = 'Фамилия не может быть пустой'
                data['errors'] = {'last_name': True}
                return Response(data, HTTP_400_BAD_REQUEST)

            if not user_data['password']:
                data['detail'] = 'Необходимо указать пароль'
                data['errors'] = {'password': True}
                return Response(data, HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(data, HTTP_400_BAD_REQUEST)

        try:
            Profile.objects.create(**profile_data)
            data['detail'] = 'Пользователь создан успешно'
            response = Response(data, HTTP_201_CREATED)
        except IntegrityError:
            data['detail'] = 'Пользователь с данной почтой уже существует'
            data['errors'] = {'email': True}
            response = Response(data, HTTP_400_BAD_REQUEST)
        except ValueError:
            data['detail'] = 'Необходимо указать электронную почту'
            data['errors'] = {'email': True}
            response = Response(data, HTTP_400_BAD_REQUEST)

        return response

    @action(methods=['get'], detail=False, url_path='detail')
    def profile_detail(self, request):
        """
        Метод для получения данных о конкретном юзере.

        :param request: объект запроса
        :return: объект ответа с данными о юзере
        """
        if request.user.is_anonymous:
            data = {'detail': 'Вам необходимо зарегистрироваться в системе'}
            return Response(data, HTTP_404_NOT_FOUND)

        serializer = UserDetailSerializer(request.user, context=self.get_serializer_context())
        return Response(serializer.data, HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def assigner(self, request):
        """
        Метод выдачи пользователей для фильтрации по заказчику.
        Ислючает из списка пользователя, сделавшего запрос.

        :param request: объект запроса
        :return: отфильтрованный кверисет
        """
        queryset = self.get_queryset() \
            .filter(is_superuser=False, is_staff=False, is_active=True) \
            .exclude(pk=request.user.pk)

        serializer = UserAssignmentSerializer(queryset, many=True, context=self.get_serializer_context())

        return Response(serializer.data, HTTP_200_OK)
