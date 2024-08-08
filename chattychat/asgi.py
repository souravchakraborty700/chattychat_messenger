import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chattychat.settings")
import django
django.setup()

from django.core.management import call_command
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # Adjust this import based on your actual app structure

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chattychat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

