"""Core app configuration."""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """App config for the core module."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        """Initialize app signals and dev helpers."""
        from .default_admin import register_default_admin

        register_default_admin()
