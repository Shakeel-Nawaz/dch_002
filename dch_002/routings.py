from django.urls import path
from app1.consumers import AsycConsumer
ws_patterns = [
    path('ws/check/',AsycConsumer.as_asgi()),
]