import os
import django
from daphne.cli import CommandLineInterface

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chattychat.settings')  # Ensure this matches your project structure

# Initialize Django
django.setup()

CommandLineInterface.entrypoint()

# run_daphne.py
# run_daphne.py
# import os
# import sys
# from daphne.cli import CommandLineInterface

# if __name__ == "__main__":
#     port = os.environ.get('PORT', '8000')
#     sys.argv = ["daphne", "-b", "0.0.0.0", "-p", port, "chattychat.asgi:application"]
#     CommandLineInterface.entrypoint()

