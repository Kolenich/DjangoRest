"""Модели приложения api."""

from django.db import models


class Employee(models.Model):
    """Модель Сотрудника."""

    SEX = [('male', 'Мужской'), ('female', 'Женский')]

    first_name = models.CharField(verbose_name='Имя', max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
    middle_name = models.CharField(verbose_name='Отчество', max_length=64, null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=32, null=True, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    sex = models.CharField(verbose_name='Пол', max_length=6, choices=SEX, default='male')
    registration_date = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('id',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
