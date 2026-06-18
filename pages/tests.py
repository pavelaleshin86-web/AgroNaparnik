from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage


class ContactViewTests(TestCase):
    def test_contact_get_returns_200(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_contact_post_does_not_create_message(self):
        response = self.client.post(
            reverse("contact"),
            {
                "name": "Иван",
                "email": "ivan@example.com",
                "message": "Нужен сайт",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)
