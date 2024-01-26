from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from accounts.models import User


class RegistrationAPITestCase(TestCase):
    fixtures = ['accounts/fixture/users.json']

    def setUp(self):
        self.client = APIClient()

    def test_registration_successful(self):
        url = '/api/user/register/'
        data = {
            "email": "sanat1234@example.com",
            "name": "SKM",
            "password": "12345678",
            "password2": "12345678"
        }
        cnt = User.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data['error'], False)
        self.assertEqual(response.data['status_code'], status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), cnt + 1)

    def test_registration_invalid_passwords(self):
        url = '/api/user/register/'
        data = {
            "email": "sanat123@example.com",
            "name": "SKM",
            "password": "12345678",
            "password2": "87654321"
        }
        cnt = User.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data['error'], True)
        self.assertEqual(response.data['status_code'], status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), cnt)

    def test_login_successful(self):
        url = '/api/user/login/'

        data = {
            "email": "sanat123@example.com",
            "password": "12345678"
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.data['error'], False)
        self.assertEqual(response.data['status_code'], status.HTTP_200_OK)
        self.assertIn('token', response.data['responseData'])
        self.assertIn('refresh', response.data['responseData']['token'])
        self.assertIn('access', response.data['responseData']['token'])

    def test_login_unsuccessful(self):
        url = '/api/user/login/'

        data = {
            "email": "sanat123@example.com",
            "password": "123456789"
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.data['error'], True)
        self.assertEqual(response.data['status_code'], status.HTTP_400_BAD_REQUEST)
