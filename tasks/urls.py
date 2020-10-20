"""Настройки URL'ов для приложения tasks."""

from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet, TaskDashboardViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'dashboard', TaskDashboardViewSet, basename='dashboard')
ROUTER.register(r'', TaskViewSet, basename='tasks')

urlpatterns = ROUTER.urls
