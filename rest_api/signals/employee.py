"""Файл сигналов для модели Employee."""

from django.db.models.signals import post_delete
from django.dispatch import receiver

from rest_api.models import Employee


@receiver(post_delete, sender=Employee)
def submission_delete(sender, instance: Employee, **kwargs):
    """
    Функция-сигнал объектов Avatar, связанных с сотрудником.

    :param sender: отправитель сигнала
    :param instance: объект удаленной модели
    :param kwargs: дополнительные аргументы
    :return:
    """

    if instance.avatar is not None:
        instance.avatar.delete()
