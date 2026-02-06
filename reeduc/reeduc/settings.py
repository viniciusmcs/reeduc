"""Compatibility settings module.

This file remains for compatibility with tools that still import
`reeduc.settings`. It delegates to the development settings module.
"""

# Import all settings from the development module to keep behavior intact.
from .settings_dev import *  # noqa: F401,F403
