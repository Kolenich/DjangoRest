"""Консумеры вебсокетов для tasks."""

from channels.generic.websocket import AsyncWebsocketConsumer


class BaseConsumer(AsyncWebsocketConsumer):
    """Базовый консумер. От него наследуются все остальные."""

    async def connect(self):
        await self.channel_layer.group_add(self.group, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group, self.channel_name)

    async def default(self, event):
        await self.send(event.get('message'))


class TaskConsumer(BaseConsumer):
    """Консумер для главной страницы со списком задач."""

    async def connect(self):
        self.group = f'tasks_{self.scope["user"].username}'
        await super().connect()
