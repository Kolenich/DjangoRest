"""Настройки URL'ов для приложения users."""

from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'', UserViewSet)

urlpatterns = ROUTER.urls
