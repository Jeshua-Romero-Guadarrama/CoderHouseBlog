# pages/models.py

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

"""
Modelos de la app 'pages'.
Aquí se define la estructura de la base de datos para las 'páginas'.
"""

class Page(models.Model):
    """
    Representa una página dentro del sitio.
    Cumple con: 2 CharField, 1 texto enriquecido, 1 imagen y 1 fecha.
    """
    title = models.CharField(
        max_length=200,
        verbose_name="Título"
    )
    subtitle = models.CharField(
        max_length=200,
        verbose_name="Subtítulo",
        blank=True,
        null=True
    )
    content = RichTextField(
        verbose_name="Contenido",
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='pages_images/',
        blank=True,
        null=True,
        verbose_name="Imagen"
    )
    created_at = models.DateField(
        verbose_name="Fecha de creación"
    )

    def __str__(self):
        """
        Representación en cadena de la página, se muestra el título.
        """
        return self.title

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['-created_at']  # Ordenar por fecha descendiente
