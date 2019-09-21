"""Настройки URL'ов для приложения users_app."""

from rest_framework.routers import DefaultRouter

from users_app.views import UserRegistrationViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'user', UserRegistrationViewSet)

urlpatterns = ROUTER.urls
