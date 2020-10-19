"""Файл с инструментами для отработки случаев изменения параметров внешнего конфига."""

import os

from django.conf import settings
from yaml import safe_load


def cut_protocol(domain: str = '') -> str:
    """
    Функция, обрезающая из домена протокол и возвращающая только хост.

    :param domain: полный домен
    :return: хост без протокола
    """
    if domain != '' and domain.split('://')[0] in ('http', 'https'):
        return domain.split('://')[1]
    return domain


def get_config_from_file(file: str):
    """
    Функция для получения распасенного конфига из переданного файла.

    :param file: файл конфига
    :return: прочитанный конфиг
    """
    if os.environ.get('PROJECT_MODE') != 'production':
        return {}
    if os.path.exists(file):
        with open(file, 'r') as ymlfile:
            config = safe_load(ymlfile)
        return config
    else:
        raise FileNotFoundError('Configuration file not found')


def get_celery_config(celery_config):
    """
    Функция получения настройки подключения к CELERY.

    :param celery_config: объект настроек CELERY
    :return: настройка подключения к CELERY
    """
    if celery_config:
        return f'amqp://{celery_config.get("USER")}:{celery_config.get("PASSWORD")}@diary-rabbitmq:5672/' \
               f'{celery_config.get("HOST")}'
    return f'sqla+sqlite:///{os.path.join(settings.BASE_DIR, "db.sqlite3")}'
