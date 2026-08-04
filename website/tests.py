from django.test import TestCase

from .models import ContactMessage


class ContactMessageModelTest(TestCase):

    def test_string_representation(self):

        message = ContactMessage.objects.create(
            name="John Doe",
            email="john@example.com",
            phone="+123456789",
            subject="Test Subject",
            message="Test message.",
        )

        self.assertEqual(
            str(message),
            "John Doe - Test Subject",
        )