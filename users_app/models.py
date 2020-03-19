"""Модели приложения users_app."""

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.db import models


class Profile(models.Model):
    """Модель Профиля пользователя."""

    user = models.OneToOneField('auth.User', models.CASCADE, verbose_name='Пользователь')
    avatar = models.OneToOneField('common_models_app.Attachment', models.SET_NULL, verbose_name='Аватар', null=True,
                                  blank=True)
    middle_name = models.CharField('Отчество', max_length=128, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=32, blank=True, null=True)
    mailing = models.BooleanField('Рассылка на почту', default=False, blank=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        ordering = ('id',)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'
