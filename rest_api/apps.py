"""Файл конфигурации приложения Django."""

from django.apps import AppConfig


class RestApiConfig(AppConfig):
    """Класс конфигурации приложения RESTAPI в Django."""

    name = 'rest_api'

    def ready(self):
        """
        Функция, вызываемая после активации приложения. Осуществляет импорт сигналов для работы с моделями.

        :return:
        """
