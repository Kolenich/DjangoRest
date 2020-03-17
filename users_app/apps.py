"""Файл конфигурации приложения UsersApp."""

from django.apps import AppConfig


class UsersApp(AppConfig):
    """Класс конфигурации приложения UsersApp в Django."""

    name = 'users_app'
    verbose_name = 'Данные о пользователях'

    def ready(self):
        """Функция, выполняемая после запуска приложения. Делает импорт сигналов для моделей."""
        # noinspection PyUnresolvedReferences
        from users_app import signals  # noqa F401
        # noinspection PyUnresolvedReferences
        from lib import custom_lookups  # noqa F401
