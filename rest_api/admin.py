"""Файл для регистрации моделей в админке."""

from django.contrib import admin

from rest_api.models import Avatar, Employee


class AvatarAdmin(admin.ModelAdmin):
    """Дополнительный класс для админки Avatar."""

    fieldsets = [
        ('Сам объект файла', {'fields': ['file']}),
        ('Мета информация', {'fields': ['file_name', 'content_type', 'size']}),
    ]
    list_display = ('file', 'file_name', 'content_type', 'size')
    list_filter = ('file_name', 'size')
    search_fields = ('file_name', 'content_type')


# Register your models here.
admin.site.register(Employee)
admin.site.register(Avatar, AvatarAdmin)
