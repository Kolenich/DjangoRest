"""Файл примесей для приложения user_auth."""
import logging

import filetype
from drf_extra_fields.fields import Base64FileField as Base64Field

LOGGER = logging.getLogger('simple_logger')


class Base64FileField(Base64Field):
    """Кастомный класс поля файлов base64."""

    # Список допустимых типов файлов
    ALLOWED_TYPES = ('jpeg', 'jpg', 'png', 'pdf')

    def get_file_extension(self, filename, decoded_file):
        """
        Переопределение функции проверки расширения файла.

        :param filename: имя файла без расширения
        :param decoded_file: поток байтов
        :return: расширение файла
        """
        # Пытаемся получить расширение файла по первым байтам
        extension = filetype.guess(decoded_file).extension

        extension = 'jpg' if extension == 'jpeg' else extension

        return extension
