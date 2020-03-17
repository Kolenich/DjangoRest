"""Сигналы для модели Attachment."""
import os

from django.db.models.signals import post_delete
from django.dispatch import receiver
from django_filters.conf import settings

from common_models_app.models import Attachment
from lib.functions import delete_empty_dirs


@receiver(post_delete, sender=Attachment)
def delete_file_from_host(sender, instance: Attachment, **kwargs):
    """Удаляет файл с хоста после удаления связанной модели."""
    instance.file.delete(False)
    delete_empty_dirs(os.path.join(settings.BASE_DIR, 'media'))
