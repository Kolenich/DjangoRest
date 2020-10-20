"""Сигналы для модели Attachment."""
import os

from django.db.models.signals import post_delete
from django.dispatch import receiver

from backend.settings import BASE_DIR
from common_models.models import Attachment
from lib.tools.functions import delete_empty_dirs


@receiver(post_delete, sender=Attachment)
def delete_file_from_host(sender, instance: Attachment, **kwargs):
    """Удаляет файл с хоста после удаления связанной модели."""
    instance.file.delete(False)
    delete_empty_dirs(os.path.join(BASE_DIR, 'media'))
