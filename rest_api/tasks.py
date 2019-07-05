"""Файл с задачами для Celery."""

from celery import shared_task


@shared_task
def sum_test(x, y):
    """
    Тестовая задача для Celery.

    :param x: число
    :param y: число
    :return: сумма x и y
    """
    return x + y
