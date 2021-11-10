"""
WSGI config for merlin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.core.asgi import get_asgi_application
from viewer.consumers import Monkey


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "merlin.settings")

application = ProtocolTypeRouter({
    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r'^viewer/$', Monkey.as_asgi())
        ])
    ),
})