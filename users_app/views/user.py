"""Файл с viewset'ами для модели User."""

from django.db.utils import IntegrityError
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from lib.mixins import ModelViewSet
from users_app.models import User
from users_app.serializers import UserAssignmentSerializer, UserProfileSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    """Базовый viewset для модели Пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def registrate(self, request: Request) -> Response:
        """
        Экшн для регистрации новых пользователей.

        :param request: объект запроса
        :return: 201 или 400
        """
        data = {'detail': 'Неверные данные'}

        try:
            if request.data['first_name'] == '':
                data['detail'] = 'Имя не может быть пустым'
                data['errors'] = {'first_name': True}
                return Response(data, HTTP_400_BAD_REQUEST)

            if request.data['last_name'] == '':
                data['detail'] = 'Фамилия не может быть пустой'
                data['errors'] = {'last_name': True}
                return Response(data, HTTP_400_BAD_REQUEST)

            if request.data['password'] == '':
                data['detail'] = 'Необходимо указать пароль'
                data['errors'] = {'password': True}
                return Response(data, HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(data, HTTP_400_BAD_REQUEST)

        try:
            User.objects.create_user(**request.data)
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

    @action(methods=['get'], detail=False)
    def profile(self, request: Request):
        """
        Метод для получения данных о конкретном юзере.

        :param request: объект запроса
        :return: объект ответа с данными о юзере
        """
        try:
            user = self.get_queryset().get(email=request.user.email)

            serializer = UserProfileSerializer(user)

            return Response(serializer.data, HTTP_200_OK)
        except User.DoesNotExist:
            data = {'detail': 'Указанный пользователь не найден'}

            return Response(data, HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=False)
    def assigner(self, request: Request):
        """
        Метод выдачи пользователей для фильтрации по заказчику.
        Ислючает из списка пользователя, сделавшего запрос.

        :param request: объект запроса
        :return: отфильтрованный кверисет
        """
        queryset = self.get_queryset().filter(
            is_superuser=False,
            is_staff=False,
            is_active=True,
            pk__ne=request.user.pk
        )

        serializer = UserAssignmentSerializer(queryset, many=True)

        return Response(serializer.data, HTTP_200_OK)
