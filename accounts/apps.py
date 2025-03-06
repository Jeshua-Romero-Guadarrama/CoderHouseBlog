# accounts/apps.py

from django.apps import AppConfig

class AccountsConfig(AppConfig):
    """
    Configuración de la aplicación 'accounts'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
