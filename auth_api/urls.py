"""Настройки URL'ов для приложения auth_api."""

from rest_framework.routers import DefaultRouter

from auth_api.views import UserViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'users', UserViewSet)

urlpatterns = ROUTER.urls
