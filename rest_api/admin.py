"""Файл для регистрации моделей в админке."""

from django.contrib import admin

from rest_api.models import Employee, Avatar

# Register your models here.
admin.site.register(Employee)
admin.site.register(Avatar)
