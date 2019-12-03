"""Сигналы для модели Attachment."""

from django.db.models.signals import post_delete
from django.dispatch import receiver

from common_models_app.models import Attachment


@receiver(post_delete, sender=Attachment)
def delete_file_from_host(sender, instance: Attachment, **kwargs):
    """Удаляет файл с хоста после удаления связанной модели."""
    instance.file.delete(False)
