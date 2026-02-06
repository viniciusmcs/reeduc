"""Production settings.

Security-focused configuration with DEBUG disabled.
"""

from .settings_base import *  # noqa: F401,F403
from .settings_base import get_env_list

# Ensure DEBUG is disabled in production.
DEBUG = False

# Security headers and HTTPS settings (override via env if needed).
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Optional: configure trusted origins via env to avoid hardcoding.
CSRF_TRUSTED_ORIGINS = get_env_list("CSRF_TRUSTED_ORIGINS", [])
