# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

"""
Modelo de la app 'accounts' para extender la información del usuario.
Por ejemplo, un modelo 'Profile' con avatar, bio, fecha de nacimiento, etc.
"""

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Usuario"
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name="Avatar"
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Biografía"
    )
    birthdate = models.DateField(
        blank=True,
        null=True,
        verbose_name="Fecha de nacimiento"
    )

    def __str__(self):
        return f"Perfil de {self.user.username}"
