"""Файл представлений модели Attachment."""

from rest_framework import viewsets

from common_models_app.models import Attachment
from common_models_app.serializers import AttachmentSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    """Базовое представление модели Attachment."""

    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
