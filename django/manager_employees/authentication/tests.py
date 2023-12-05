from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='manager', password='12345678'
        )
        self.client = Client()

    def test_user_login(self):
        response = self.client.post(reverse('user_login'), {'username': 'manager', 'password': '12345678'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('departments'))

    def test_user_login_invalid_credentials(self):
        response = self.client.post(reverse('user_login'), {'username': 'manager1', 'password': '12345678'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid login credentials')

    def test_user_logout(self):
        self.client.login(username='manager', password='12345678')
        response = self.client.get(reverse('user_logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user_login'))
