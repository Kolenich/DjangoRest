"""Настройки URL'ов для приложения users_app."""

from rest_framework.routers import DefaultRouter

from users_app.views import UserViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'user', UserViewSet)

urlpatterns = ROUTER.urls
