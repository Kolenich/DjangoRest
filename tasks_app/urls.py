"""Настройки URL'ов для приложения tasks_app."""

from rest_framework.routers import DefaultRouter

from tasks_app.views import AssignedTaskViewSet, TaskDetailViewSet, TaskTableViewset

ROUTER = DefaultRouter()

ROUTER.register(r'task-detail', TaskDetailViewSet)
ROUTER.register(r'task-table', TaskTableViewset)
ROUTER.register(r'assign-task', AssignedTaskViewSet)

urlpatterns = ROUTER.urls
