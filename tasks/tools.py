"""Дополнительные инструменты для приложения tasks."""
from background_task import background, models
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


@background(queue='email')
def send_email(subject, html, receivers, copy=list):
    msg = EmailMultiAlternatives(subject, strip_tags(html), settings.EMAIL_FROM, receivers, cc=copy)
    msg.attach_alternative(html, 'text/html')
    msg.send()
