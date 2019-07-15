"""Файл с задачами для Celery."""

from celery import shared_task
from django.core.mail import EmailMessage

from backend import settings
from rest_api.models import Employee
from tools.email_messages import greetings_body


@shared_task
def greetings_via_email(employee: Employee):
    """
    Задача для отпаравки писем приветствия.

    :param employee: сотрудник, которого надо поприветствовать
    """
    message = EmailMessage(
        settings.GREETINGS_SUBJECT,
        greetings_body(employee.first_name, employee.middle_name),
        settings.EMAIL_HOST_USER,
        [employee.email]
    )
    message.content_subtype = 'html'
    message.send()
