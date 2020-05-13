"""Настройки URL'ов для приложения tasks_app."""

from rest_framework.routers import DefaultRouter

from tasks_app.views import TaskViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'tasks', TaskViewSet)

urlpatterns = ROUTER.urls
