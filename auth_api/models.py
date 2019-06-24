"""Модели приложения auth_api."""

import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager


def save_join_date(sender, user, **kwargs):
    """Дергается по сигналу входа пользователя, если это первый вход юзера, то фиксируется в бд."""
    if user.join_date is None:
        user.join_date = timezone.now()
        user.save(update_fields=['join_date'])


user_logged_in.connect(save_join_date)


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя. Используется вместо стандартной джанговской модели."""

    uid = models.UUIDField(verbose_name='UID пользователя', editable=False, unique=True, default=uuid.uuid4)
    is_active = models.BooleanField(verbose_name='Пользователь активен', default=True, blank=True)
    is_staff = models.BooleanField(verbose_name='Статус админа', default=False, blank=True)
    is_superuser = models.BooleanField(verbose_name='Статус супер-админа', default=False, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=128)
    first_name = models.CharField(verbose_name='Имя', max_length=128)
    middle_name = models.CharField(verbose_name='Отчество', max_length=128, blank=True, null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=32, blank=True, null=True)
    email = models.CharField(verbose_name='Почта', max_length=128, unique=True)
    join_date = models.DateTimeField(verbose_name='Дата первого входа', blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, blank=True, editable=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'
