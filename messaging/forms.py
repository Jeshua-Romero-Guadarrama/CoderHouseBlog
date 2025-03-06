# messaging/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Message

"""
Formularios de la aplicación 'messaging'.
Incluye un formulario para crear un nuevo mensaje.
"""

class MessageForm(forms.ModelForm):
    """
    Formulario para enviar un mensaje a otro usuario.
    """
    # Personalizamos el campo 'to_user' para elegir destinatario de entre los usuarios existentes.
    to_user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Enviar a"
    )

    class Meta:
        model = Message
        fields = ['to_user', 'subject', 'body']
        labels = {
            'subject': 'Asunto',
            'body': 'Contenido del mensaje'
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
