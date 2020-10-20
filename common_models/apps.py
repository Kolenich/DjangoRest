"""Файл конфигурации приложения CommonModelsApp."""

from django.apps import AppConfig


class CommonModelsAppConfig(AppConfig):
    """Класс конфигурации приложение."""

    name = 'common_models'
    verbose_name = 'Данные о вспомогательных моделях'

    def ready(self):
        """Функция, выполняемая после запуска приложения. Делает импорт сигналов для моделей."""
        # noinspection PyUnresolvedReferences
        from common_models import signals  # noqa F401
