"""Модели приложения users."""

from django.db import models


class Profile(models.Model):
    """Модель Профиля пользователя."""

    user = models.OneToOneField('auth.User', models.CASCADE, verbose_name='Пользователь')
    avatar = models.OneToOneField('common_models.Attachment', models.SET_NULL, verbose_name='Аватар', null=True,
                                  blank=True)
    middle_name = models.CharField('Отчество', max_length=128, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=32, blank=True, null=True)
    mailing = models.BooleanField('Рассылка на почту', default=False, blank=True)

    @property
    def full_name(self):
        """Свойство получения полного имени."""
        if self.middle_name:
            return f'{self.user.last_name} {self.user.first_name} {self.middle_name}'
        return f'{self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        db_table = 'profiles'

    def __str__(self):
        return f'Профиль {self.user.username}'
