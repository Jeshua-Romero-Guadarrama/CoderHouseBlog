# blog/admin.py

from django.contrib import admin
from .models import Post

"""
En este archivo se registran los modelos de la app 'blog' 
para gestionarlos desde el panel de administración de Django.
"""

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Configuración del modelo 'Post' en el admin de Django.
    """
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')
