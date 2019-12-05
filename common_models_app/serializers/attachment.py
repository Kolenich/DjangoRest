"""Сериалайзеры модели Attachment."""

from rest_framework import serializers

from common_models_app.models import Attachment
from mixins import Base64FileField


class AttachmentSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Attachment."""

    file = Base64FileField()

    class Meta:
        model = Attachment
        fields = '__all__'
