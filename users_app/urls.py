"""Настройки URL'ов для приложения users_app."""

from rest_framework.routers import DefaultRouter

from users_app.views import ProfileViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'profile', ProfileViewSet)

urlpatterns = ROUTER.urls
