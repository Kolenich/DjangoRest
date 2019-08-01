"""Настройки URL'ов для приложения rest_api."""

from rest_framework.routers import DefaultRouter

from rest_api.views import AvatarViewSet, EmployeeTableViewSet, EmployeeViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'employee', EmployeeViewSet)
ROUTER.register(r'employee-table', EmployeeTableViewSet)
ROUTER.register(r'avatar', AvatarViewSet)

urlpatterns = ROUTER.urls
