# messaging/models.py

from django.db import models
from django.contrib.auth.models import User

"""
Modelo principal de la app 'messaging' para gestionar mensajes entre usuarios.
"""

class Message(models.Model):
    """
    Representa un mensaje enviado de un usuario a otro.
    """
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        verbose_name="Remitente"
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_messages',
        verbose_name="Destinatario"
    )
    subject = models.CharField(
        max_length=200,
        verbose_name="Asunto"
    )
    body = models.TextField(
        verbose_name="Contenido"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de envío"
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name="Leído"
    )

    def __str__(self):
        """
        Devuelve una representación en cadena del mensaje.
        """
        return f"De {self.from_user} para {self.to_user} - Asunto: {self.subject}"

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ['-created_at']
