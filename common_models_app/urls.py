"""Настройки URL'ов для приложения CommonModelsApp."""

from rest_framework.routers import DefaultRouter

from common_models_app.views import AttachmentViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'attachment', AttachmentViewSet)

urlpatterns = ROUTER.urls
