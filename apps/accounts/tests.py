from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import authenticate
from .models import User
from apps.todo.jwt_utils import decode_jwt


class AccountsTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_and_authenticate(self):
        user = User.objects.create_user(username='bob', email='bob@example.com', password='secret')
        self.assertTrue(user.check_password('secret'))

        # authenticate by email
        u = authenticate(email='bob@example.com', password='secret')
        self.assertIsNotNone(u)
        self.assertEqual(u.email, 'bob@example.com')

    def test_register_and_login_endpoints(self):
        resp = self.client.post('/auth/register/', {'username': 'alice', 'email': 'alice@example.com', 'password': 'pw123'})
        self.assertEqual(resp.status_code, 201)

        resp = self.client.post('/auth/login/', {'email': 'alice@example.com', 'password': 'pw123'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn('token', resp.json())

        token = resp.json()['token']
        decoded = decode_jwt(token)
        self.assertEqual(decoded['user_id'], User.objects.get(email='alice@example.com').id)
