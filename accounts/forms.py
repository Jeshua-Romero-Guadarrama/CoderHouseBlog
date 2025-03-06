# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

"""
Formularios para la app 'accounts':
- Formulario de registro de usuario (UserCreationForm).
- Formulario de actualización de perfil.
"""

class UserRegisterForm(UserCreationForm):
    """
    Formulario para registrar un nuevo usuario.
    Incluye campos de username, email y password.
    """
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

class ProfileForm(forms.ModelForm):
    """
    Formulario para actualizar datos del perfil.
    """
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birthdate']
        labels = {
            'avatar': 'Avatar',
            'bio': 'Biografía',
            'birthdate': 'Fecha de nacimiento',
        }
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }
