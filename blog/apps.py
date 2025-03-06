# blog/apps.py

from django.apps import AppConfig

class BlogConfig(AppConfig):
    """
    Configuración de la aplicación 'blog'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
