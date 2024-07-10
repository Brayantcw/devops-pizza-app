"""
This module contains the app configuration for the myapp application.
"""

from django.apps import AppConfig

class MyappConfig(AppConfig):
    """
    default apps module
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
