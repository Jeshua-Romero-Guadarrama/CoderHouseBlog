# blog/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

"""
Módulo de pruebas para la aplicación 'blog'.
Las pruebas ayudan a asegurar que las funcionalidades se comporten según lo esperado.
"""

class PostModelTest(TestCase):
    """
    Prueba básica del modelo 'Post'.
    """

    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Crear un post de prueba
        self.post = Post.objects.create(
            title='Título de prueba',
            content='Contenido de prueba',
            author=self.user
        )

    def test_post_str(self):
        """
        Verifica que la representación en string del post sea el título.
        """
        self.assertEqual(str(self.post), 'Título de prueba')

    def test_post_author_is_correct(self):
        """
        Verifica que el autor del post sea el usuario de prueba.
        """
        self.assertEqual(self.post.author.username, 'testuser')
