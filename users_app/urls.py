"""Настройки URL'ов для приложения users_app."""

from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from users_app.views import UserAssignmentViewset, UserProfileViewSet, UserRegistrationViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'user', UserRegistrationViewSet)
ROUTER.register(r'user-assigner', UserAssignmentViewset)
ROUTER.register(r'user-profile', UserProfileViewSet)

urlpatterns = [
    url(r'', include(ROUTER.urls)),
]
