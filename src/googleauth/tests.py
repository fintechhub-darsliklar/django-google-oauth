from django.test import TestCase  # noqa: F401
from django.contrib.auth.models import User

# Create your tests here.

class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="12345"
        )

    def test_login(self):
        logged_in = self.client.login(
            username="testuser",
            password="12345"
        )
        self.assertTrue(logged_in)


class DashboardTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="12345"
        )

    def test_dashboard_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_login_to_dashboard_page(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

