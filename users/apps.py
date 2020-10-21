"""Файл конфигурации приложения UsersApp."""

from django.apps import AppConfig


class UsersApp(AppConfig):
    """Класс конфигурации приложения UsersApp в Django."""

    name = 'users'
    verbose_name = 'Данные о пользователях'

    def ready(self):
        """Функция, выполняемая после запуска приложения. Делает импорт сигналов для моделей."""
        # noinspection PyUnresolvedReferences
        import custom_lookups
        # noinspection PyUnresolvedReferences
        from users import signals  # noqa F401
