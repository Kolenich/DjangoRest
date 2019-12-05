"""Файл конфигурации приложения TasksApp."""

from django.apps import AppConfig


class TasksAppConfig(AppConfig):
    """Класс конфигурации приложение."""

    name = 'tasks_app'
    verbose_name = 'Данные о заданиях'

    def ready(self):
        """Функция, выполняемая после запуска приложения. Делает импорт сигналов для моделей."""
        # noinspection PyUnresolvedReferences
        from tasks_app import signals  # noqa F401
