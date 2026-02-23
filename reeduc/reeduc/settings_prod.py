"""Production settings.

Security-focused configuration with DEBUG disabled.
"""

from .settings_base import *  # noqa: F401,F403
from .settings_base import get_env_list

# Ensure DEBUG is disabled in production.
DEBUG = False

# Internal network deployment over HTTP.
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_CONTENT_TYPE_NOSNIFF = True

# Optional: configure trusted origins via env to avoid hardcoding.
CSRF_TRUSTED_ORIGINS = get_env_list("CSRF_TRUSTED_ORIGINS", ["http://10.0.125.4"])
