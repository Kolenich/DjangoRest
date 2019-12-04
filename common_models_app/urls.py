"""Настройки URL'ов для приложения CommonModelsApp."""

from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from common_models_app.views import AttachmentViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'attachment', AttachmentViewSet)

urlpatterns = [
    url(r'', include(ROUTER.urls)),
]
