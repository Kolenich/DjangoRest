"""Модели приложения CommonModelsApp."""

from django.db import models


class Attachment(models.Model):
    """Модель вложения."""

    file = models.FileField('Файл', upload_to='attachments')
    file_name = models.CharField('Имя файла', max_length=64)
    file_mime = models.CharField('Тип файла', max_length=128)
    file_size = models.PositiveIntegerField('Размер файла')

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
        db_table = 'attachments'

    def __str__(self):
        return self.file_name
