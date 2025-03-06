# pages/forms.py

from django import forms
from .models import Page

"""
Formularios de la aplicación 'pages'.
Se definen formularios basados en modelos o formularios personalizados.
"""

class PageForm(forms.ModelForm):
    """
    Formulario para crear o editar instancias del modelo 'Page'.
    """
    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'content', 'image', 'created_at']
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'content': 'Contenido',
            'image': 'Imagen',
            'created_at': 'Fecha de creación',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }
