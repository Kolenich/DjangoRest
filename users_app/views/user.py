"""Файл с viewset'ами для модели User."""

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from users_app.models import Profile
from users_app.serializers import ProfileAssignmentSerializer, ProfileDetailSerializer, ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """Базовый viewset для модели Пользователя."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def registrate(self, request: Request) -> Response:
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
            'middle_name': request.data.pop('middle_name', False)
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
            Profile.objects.create(user=User.objects.create_user(**user_data), **profile_data)
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
    def profile_detail(self, request: Request):
        """
        Метод для получения данных о конкретном юзере.

        :param request: объект запроса
        :return: объект ответа с данными о юзере
        """
        try:
            profile = self.get_queryset().get(user=User.objects.get(username=request.user.username))

            serializer = ProfileDetailSerializer(profile)

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
            user__is_superuser=False,
            user__is_staff=False,
            user__is_active=True,
            user__pk__ne=request.user.pk
        )

        serializer = ProfileAssignmentSerializer(queryset, many=True)

        return Response(serializer.data, HTTP_200_OK)
