"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import importlib
import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from websockets.routing import urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django_asgi_app = get_asgi_application()

middleware = importlib.import_module('websockets.middleware')
middleware_stack = getattr(middleware, 'middleware_stack')

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': middleware_stack(
        URLRouter(
            urlpatterns
        )
    ),
})
