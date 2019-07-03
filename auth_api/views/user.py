"""Файл с viewset'ами для модели User."""

from rest_framework import viewsets

from auth_api.models import User
from auth_api.serializers import BaseUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Базовый viewset для модели Пользователя."""

    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
