# accounts/admin.py

from django.contrib import admin
from .models import Profile

"""
Registro de modelos de la app 'accounts' en el panel de administración.
"""

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Configuración de la administración del modelo 'Profile'.
    """
    list_display = ('user', 'bio', 'birthdate')
    search_fields = ('user__username', 'bio')
