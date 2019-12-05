"""Сигналы для модели Task."""

from django.db.models.signals import post_delete
from django.dispatch import receiver

from tasks_app.models import Task


@receiver(post_delete, sender=Task)
def delete_attachment(sender, instance: Task, **kwargs):
    """Удаляет вложение."""
    instance.attachment.delete()
