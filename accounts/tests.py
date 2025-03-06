# accounts/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

"""
Pruebas unitarias para la app 'accounts'.
"""

class ProfileTest(TestCase):
    """
    Prueba básica para la creación de un perfil.
    """
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='testpass')
        self.profile = Profile.objects.create(user=self.user, bio="Bio de prueba")

    def test_profile_str(self):
        """
        Verifica la representación string del perfil.
        """
        self.assertEqual(str(self.profile), "Perfil de tester")
