"""Настройки URL'ов для приложения CommonModelsApp."""

from rest_framework.routers import DefaultRouter

from common_models.views import AttachmentViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'attachment', AttachmentViewSet)

urlpatterns = ROUTER.urls
