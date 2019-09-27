"""Сигналы для модели User."""

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone

from users_app.models import User


@receiver(user_logged_in, sender=User)
def save_join_date(sender, user: User, **kwargs):
    """Дергается по сигналу входа пользователя, если это первый вход юзера, то фиксируется в бд."""
    if user.join_date is None:
        user.join_date = timezone.now()
        user.save(update_fields=['join_date'])
