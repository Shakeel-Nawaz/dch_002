"""
ASGI config for dch_002 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from .routings import ws_patterns
from channels.routing import ProtocolTypeRouter, URLRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dch_002.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket' : URLRouter(ws_patterns)
}) 
