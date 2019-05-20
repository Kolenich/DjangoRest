from rest_framework import viewsets
from API.models import Attachment
from API.serializers import AttachmentSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Customer
    """
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
