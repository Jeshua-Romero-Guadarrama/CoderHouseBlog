# blog/models.py

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  # Si usas Django CKEditor para texto enriquecido

"""
Aquí se definen los modelos (tablas) para la aplicación 'blog'.
Cada clase de modelo representa una entidad de la base de datos.
"""

class Post(models.Model):
    """
    Modelo que representa una publicación de blog.
    """
    title = models.CharField(
        max_length=200,
        verbose_name="Título"
    )
    content = RichTextField(
        verbose_name="Contenido",
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Autor"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    image = models.ImageField(
        upload_to='posts_images/',
        blank=True,
        null=True,
        verbose_name="Imagen"
    )

    def __str__(self):
        """
        Devuelve el título del post al representarlo como cadena.
        """
        return self.title

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-created_at']
