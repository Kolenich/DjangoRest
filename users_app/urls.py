"""Настройки URL'ов для приложения users_app."""

from rest_framework.routers import DefaultRouter

from users_app.views import UserAssignerViewset, UserRegistrationViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'user', UserRegistrationViewSet)
ROUTER.register(r'user-assigner', UserAssignerViewset)

urlpatterns = ROUTER.urls
