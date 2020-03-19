"""Сигналы для модели Profile."""

from django.db.models.signals import post_delete
from django.dispatch import receiver

from users_app.models import Profile


@receiver(post_delete, sender=Profile)
def delete_avatar(sender, instance: Profile, **kwargs):
    """Удаляет аватар."""
    instance.avatar.delete()
