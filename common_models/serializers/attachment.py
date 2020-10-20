"""Сериалайзеры модели Attachment."""

from rest_framework import serializers

from common_models.models import Attachment


class AttachmentSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Attachment."""

    class Meta:
        model = Attachment
        fields = '__all__'
