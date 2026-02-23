"""Development settings.

Keep DEBUG on for local development and allow localhost hosts.
"""

from .settings_base import *  # noqa: F401,F403

# Enable debug in development.
DEBUG = True

# Allow local hosts explicitly in development.
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "10.0.125.4"]
