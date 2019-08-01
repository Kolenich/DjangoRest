"""Файл сигналов для модели Avatar."""

from django.db.models.signals import post_delete
from django.dispatch import receiver

from rest_api.models import Avatar


@receiver(post_delete, sender=Avatar)
def submission_delete(sender, instance: Avatar, **kwargs):
    """
    Функция-сигнал для удаления файлов из файловой системы.

    :param sender: отправитель сигнала
    :param instance: объект удаленной модели
    :param kwargs: дополнительные аргументы
    :return:
    """
    instance.file.delete(False)
