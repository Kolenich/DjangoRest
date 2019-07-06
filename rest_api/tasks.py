"""Файл с задачами для Celery."""

from backend.celery import app


@app.task()
def sum_test(x, y):
    """
    Тестовая задача для Celery.

    :param x: число
    :param y: число
    :return: сумма x и y
    """
    print(x + y)
    return x + y
