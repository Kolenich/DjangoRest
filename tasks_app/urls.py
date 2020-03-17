"""Настройки URL'ов для приложения tasks_app."""

from rest_framework.routers import DefaultRouter

from tasks_app.views import TaskTableViewset, TaskViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'task', TaskViewSet)
ROUTER.register(r'task-table', TaskTableViewset)

urlpatterns = ROUTER.urls
