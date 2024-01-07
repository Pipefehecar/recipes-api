"""
Core app configuration module

"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Core app configuration class
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
