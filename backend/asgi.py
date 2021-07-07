import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from websockets.middleware import middleware_stack
from websockets.routing import urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': middleware_stack(
        URLRouter(
            urlpatterns
        )
    ),
})
