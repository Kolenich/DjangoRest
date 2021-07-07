"""Маршруты веб-сокетов."""

from django.urls import path

from websockets.consumers import TaskConsumer

urlpatterns = [
    path('ws/tasks/', TaskConsumer.as_asgi()),
]
