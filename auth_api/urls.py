"""Настройки URL'ов для приложения auth_api."""

from rest_framework.routers import DefaultRouter

from auth_api.views import UserRegistrationViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'user', UserRegistrationViewSet)

urlpatterns = ROUTER.urls
