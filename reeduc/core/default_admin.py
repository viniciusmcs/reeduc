"""Create a default admin user in development when configured via env.

This keeps onboarding simple without hardcoding credentials in code.
"""

import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate


def get_default_admin_data() -> dict | None:
    """Return default admin credentials from environment or None."""
    username = os.getenv("DEFAULT_ADMIN_USERNAME")
    password = os.getenv("DEFAULT_ADMIN_PASSWORD")
    email = os.getenv("DEFAULT_ADMIN_EMAIL", "admin@example.com")

    if not username or not password:
        return None

    return {
        "username": username,
        "password": password,
        "email": email,
    }


def ensure_default_admin_exists() -> None:
    """Create a default admin user if missing (dev only)."""
    if not settings.DEBUG:
        return

    data = get_default_admin_data()
    if not data:
        return

    User = get_user_model()
    if User.objects.filter(username=data["username"]).exists():
        return

    user = User.objects.create_user(username=data["username"], email=data["email"])
    user.set_password(data["password"])
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()


def create_default_admin(**kwargs) -> None:
    """Create a default admin user after migrations are applied."""
    ensure_default_admin_exists()


def register_default_admin() -> None:
    """Register the post-migrate hook for default admin creation."""
    post_migrate.connect(create_default_admin, dispatch_uid="core_create_default_admin")
