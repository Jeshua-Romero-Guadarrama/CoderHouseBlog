# pages/admin.py

from django.contrib import admin
from .models import Page

"""
Registro de modelos de la app 'pages' en el panel de administración de Django.
"""

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """
    Configuraciones para la administración de 'Page'.
    """
    list_display = ('title', 'subtitle', 'created_at')
    search_fields = ('title', 'subtitle', 'content')
    list_filter = ('created_at',)
