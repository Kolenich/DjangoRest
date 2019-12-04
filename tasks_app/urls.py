"""Настройки URL'ов для приложения tasks_app."""

from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from tasks_app.views import AssignedTaskViewSet, TaskDetailViewSet, TaskTableViewset, TaskViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'task', TaskViewSet)
ROUTER.register(r'task-detail', TaskDetailViewSet)
ROUTER.register(r'task-table', TaskTableViewset)
ROUTER.register(r'assign-task', AssignedTaskViewSet)

urlpatterns = [
    url(r'', include(ROUTER.urls)),
]
