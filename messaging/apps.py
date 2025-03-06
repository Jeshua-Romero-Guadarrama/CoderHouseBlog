# messaging/apps.py

from django.apps import AppConfig

class MessagingConfig(AppConfig):
    """
    Configuración de la aplicación 'messaging'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messaging'
