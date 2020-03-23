"""Файл с задачами для Celery."""

from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage

from lib.tools import greetings_body


@shared_task
def task_assigned_notification(email: str, task: dict, assigned_by: str):
    """
    Задача для отправки писем оповещения о назначении задания.

    :param email: электронная почта
    :param task: объект задачи
    :param assigned_by: фамилия и имя назначившего
    :return: HTML-шаблон, преобразованный в строку
    """
    message = EmailMessage(
        settings.TASK_ASSIGNED_SUBJECT,
        greetings_body(task, assigned_by),
        settings.EMAIL_HOST_USER,
        [email]
    )
    message.content_subtype = 'html'
    message.send()
