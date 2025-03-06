# messaging/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message

"""
Pruebas unitarias para la aplicación 'messaging'.
"""

class MessageModelTest(TestCase):
    """
    Pruebas básicas para el modelo 'Message'.
    """
    def setUp(self):
        self.user1 = User.objects.create_user(username='alice', password='pass123')
        self.user2 = User.objects.create_user(username='bob', password='pass123')
        self.message = Message.objects.create(
            from_user=self.user1,
            to_user=self.user2,
            subject="Prueba",
            body="Contenido de prueba"
        )

    def test_message_str(self):
        """
        Verifica la representación en cadena del mensaje.
        """
        expected_str = f"De {self.user1} para {self.user2} - Asunto: Prueba"
        self.assertEqual(str(self.message), expected_str)

    def test_message_defaults(self):
        """
        Verifica que el mensaje recién creado no esté leído.
        """
        self.assertFalse(self.message.is_read)
