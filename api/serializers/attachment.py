from rest_framework import serializers
from api.models import Attachment


class BaseAttachmentSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер для модели Attachment."""

    class Meta:
        model = Attachment
        fields = '__all__'
