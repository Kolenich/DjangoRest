"""Регистрация моделей приложения в админке."""

from django.contrib import admin

from tasks_app.models import Task

admin.site.register(Task)
