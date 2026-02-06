"""Basic tests for the core app."""

from django.test import TestCase
from django.urls import reverse


class LoginPageTests(TestCase):
    """Smoke tests for the login page."""

    def test_login_page_renders(self):
        """Ensure the login page returns HTTP 200."""
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
