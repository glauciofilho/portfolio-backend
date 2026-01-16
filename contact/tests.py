from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from .models import ContactMessage


class ContactEndpointTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/contact/form/"

        self.payload = {
            "name": "John Doe",
            "email": "john@example.com",
            "message": "Hello, this is a test message"
        }

    def test_contact_post_success(self):
        response = self.client.post(
            self.url,
            data=self.payload,
            content_type="application/json"
        )

        # ✅ Status OK
        self.assertEqual(response.status_code, 201)

        # ✅ Mensagem salva no banco
        self.assertEqual(ContactMessage.objects.count(), 1)

        msg = ContactMessage.objects.first()

        self.assertEqual(msg.name, self.payload["name"])
        self.assertEqual(msg.email, self.payload["email"])
        self.assertEqual(msg.message, self.payload["message"])

    def test_contact_post_missing_fields(self):
        response = self.client.post(
            self.url,
            data={"email": "test@test.com"},
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_contact_get_not_allowed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)