# blog/forms.py

from django import forms
from .models import Post

"""
En este archivo se definen los formularios para la aplicación 'blog'.
Formularios basados en modelos (ModelForm) o formularios personalizados.
"""

class PostForm(forms.ModelForm):
    """
    Formulario para crear o editar instancias del modelo 'Post'.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        # Opcionalmente, define labels, widgets, etc.
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'image': 'Imagen destacada',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
