"""Модели приложения api."""

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Employee(models.Model):
    """Модель Сотрудника."""

    SEX = [('male', 'Мужской'), ('female', 'Женский')]

    first_name = models.CharField(verbose_name='Имя', max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
    middle_name = models.CharField(verbose_name='Отчество', max_length=64, null=True, blank=True)
    full_name = models.CharField(verbose_name='ФИО', max_length=128)
    phone = models.CharField(verbose_name='Телефон', max_length=32, null=True, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    sex = models.CharField(verbose_name='Пол', max_length=6, choices=SEX, default='male')
    registration_date = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    avatar = models.OneToOneField('Avatar', verbose_name='Аватар', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('id',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Avatar(models.Model):
    """Модель Аватара."""

    file = models.ImageField(verbose_name='Файл', upload_to='avatars')
    content_type = models.CharField(verbose_name='Тип файла', max_length=16)
    size = models.PositiveIntegerField(verbose_name='Размер файла')
    file_name = models.CharField(verbose_name='Имя файла', max_length=1024)

    class Meta:
        verbose_name = 'Аватар'
        verbose_name_plural = 'Аватары'
        ordering = ('id',)

    def __str__(self):
        return f'{self.file_name}'


@receiver(post_delete, sender=Avatar)
def submission_delete(sender, instance: Avatar, **kwargs):
    """
    Функция-сигнал для удаления файлов из файловой системы.

    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.file.delete(False)
