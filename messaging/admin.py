# messaging/admin.py

from django.contrib import admin
from .models import Message

"""
Registro del modelo 'Message' en el panel de administración de Django.
"""

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Configuración del modelo 'Message' en el admin.
    """
    list_display = ('subject', 'from_user', 'to_user', 'created_at', 'is_read')
    list_filter = ('created_at', 'is_read')
    search_fields = ('subject', 'body', 'from_user__username', 'to_user__username')
