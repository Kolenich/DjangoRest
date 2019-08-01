"""ViewSet'ы для модели Avatar."""

from rest_framework import viewsets

from rest_api.models import Avatar
from rest_api.serializers import AvatarSerializer


class AvatarViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Avatar."""

    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
