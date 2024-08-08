"""
WSGI config for social_chat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chattychat.settings')

application = get_wsgi_application()
