"""Файл с задачами для Celery."""

from celery import shared_task
from django.core.mail import send_mail

from backend import settings


@shared_task
def send_email(to: str, msg: str, subject: str):
    """
    Задача для отпаравки писем.

    :param to: Email, на который необходимо отправить письмо
    :param msg: Текст сообщения
    :param subject: Тема письма
    """
    send_mail(
        subject=subject,
        message=msg,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to]
    )
