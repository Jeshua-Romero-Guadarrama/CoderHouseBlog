# pages/tests.py

from django.test import TestCase
from .models import Page

"""
Pruebas unitarias para la aplicación 'pages'.
"""

class PageModelTest(TestCase):
    """
    Prueba simple del modelo 'Page'.
    """
    def setUp(self):
        self.page = Page.objects.create(
            title="Página de prueba",
            subtitle="Subtítulo de prueba",
            content="Contenido de prueba",
            created_at="2025-01-01"
        )

    def test_page_str(self):
        """
        Verifica que el método __str__ retorne el título de la página.
        """
        self.assertEqual(str(self.page), "Página de prueba")
