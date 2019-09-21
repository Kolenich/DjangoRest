"""Файл для регистрации моделей в админке."""

from django.contrib import admin

from users_app.models import User

# Register your models here.
admin.site.register(User)
