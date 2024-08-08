import os
import django
from daphne.cli import CommandLineInterface

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chattychat.settings')

# # Initialize Django
# django.setup()

# # Get the port from the environment variable
# port = os.environ.get('PORT', '8000')

# CommandLineInterface.entrypoint(['daphne', '-b', '0.0.0.0', '-p', port, 'chattychat.asgi:application'])

# Initialize Django
django.setup()

CommandLineInterface.entrypoint()
