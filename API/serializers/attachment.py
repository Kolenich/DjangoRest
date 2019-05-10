from rest_framework import serializers
from API.models import Attachment


class AttachmentSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели Attachment
    """
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Attachment
        fields = '__all__'
