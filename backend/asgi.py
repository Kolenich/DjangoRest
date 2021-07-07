import os
from http.cookies import SimpleCookie

from channels.auth import AuthMiddlewareStack
from channels.db import database_sync_to_async
from channels.routing import ProtocolTypeRouter, URLRouter
from django.contrib.auth.models import AnonymousUser
from django.core.asgi import get_asgi_application
from rest_framework.authtoken.models import Token

from backend.routing import urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')


@database_sync_to_async
def get_user(token):
    """Функция получения пользователя по токену."""
    try:
        return Token.objects.get(key=token).user
    except Token.DoesNotExist:
        return AnonymousUser()


class TokenAuthMiddleware:
    """Класс-прослойка для авторизации по токену и получении пользователя."""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        cookie = SimpleCookie()
        cookie.load(dict(scope['headers']).get(b'cookie').decode())

        token = cookie['token'].value
        scope['user'] = await get_user(token)

        return await self.app(scope, receive, send)


def middleware_stack(inner):
    """Функция-обертка для компоновки прослоек."""
    return TokenAuthMiddleware(AuthMiddlewareStack(inner))


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': middleware_stack(
        URLRouter(
            urlpatterns
        )
    ),
})
