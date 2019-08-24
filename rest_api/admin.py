"""Файл для регистрации моделей в админке."""

from django.contrib import admin
from django.utils.html import format_html

from rest_api.models import Avatar, Employee


class AvatarAdmin(admin.ModelAdmin):
    """Дополнительный класс для админки Avatar."""

    def image_tag(self, instance: Avatar):
        """
        Функция для показа изображений в админке.

        :param instance: модель с полем FileField
        :return: HTML-строка с изображением
        """
        return format_html(f'<img src="{instance.file.url}" height="200px" width="auto" />')

    image_tag.short_description = 'Файл'
    fieldsets = [
        ('Сам объект файла', {'fields': ['file']}),
        ('Мета информация', {'fields': ['file_name', 'content_type', 'size']}),
    ]
    list_display = ('file_name', 'content_type', 'size', 'image_tag')
    list_filter = ('file_name', 'size')
    search_fields = ('file_name', 'content_type')
    readonly_fields = ('file_name', 'content_type', 'size', 'file')


# Register your models here.
admin.site.register(Employee)
admin.site.register(Avatar, AvatarAdmin)
