"""Класс для публикации через вебсокет."""
import json

from asgiref.sync import async_to_sync
from channels.layers import DEFAULT_CHANNEL_LAYER, get_channel_layer
from django.core.serializers.json import DjangoJSONEncoder


class Publisher:
    """Класс, отправляющий по вебсокету в указанную группу переданное сообщение."""

    def __init__(self, group):
        self.group = group
        self.layer = get_channel_layer()

    def publish(self, message=None, type_=DEFAULT_CHANNEL_LAYER):
        """Метод для непосредственной отправки сообщения по вебсокету."""
        if message is None:
            message = {}

        data_to_send = {'type': type_, 'message': json.dumps(message, cls=DjangoJSONEncoder)}
        async_to_sync(self.layer.group_send)(self.group, data_to_send)
