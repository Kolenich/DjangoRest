"""Дополнительные инструменты для приложения tasks."""
from background_task import background
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


@background(queue='email')
def send_email(subject, html, receivers, copy=None):
    """
    Функция отправки электронной почты.

    :param subject: заголовок письма
    :param html: тело письма в формате html
    :param receivers: список получателей
    :param copy: список в копию
    """
    if copy is None:
        copy = []
    msg = EmailMultiAlternatives(subject, strip_tags(html), settings.EMAIL_HOST_USER, receivers, cc=copy)
    msg.attach_alternative(html, 'text/html')
    msg.send()
