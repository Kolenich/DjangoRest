"""Файл с задачами для Celery."""

from celery import shared_task
from django.core.mail import EmailMessage

from backend import settings
from tools.email_messages import greetings_body


@shared_task
def greetings_via_email(email: str, first_name: str, middle_name: str or None):
    """
    Задача для отпаравки писем приветствия.

    :param email: электронная почта
    :param first_name: имя
    :param middle_name: отчество
    :return: HTML-шаблон, преобразованный в строку
    """
    message = EmailMessage(
        settings.GREETINGS_SUBJECT,
        greetings_body(first_name, middle_name),
        settings.EMAIL_HOST_USER,
        [email]
    )
    message.content_subtype = 'html'
    message.send()
