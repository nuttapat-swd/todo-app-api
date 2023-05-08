from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APIClient
from oauth2_provider.models import Application, AccessToken

import pytz

import datetime
# USER_URL = reverse('user:user-list')

class PublicUserTest(TestCase):
    """Test for user urls"""
    def test_get_user_urls(self):
        """Test get user urls"""
        self.client = APIClient()
        url = reverse('user:user-list')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateUserTest(TestCase):
    """Test for get urls"""
    def setUp(self):
        self.client = APIClient()
        user_payload = {
            'email': 'test@example.com',
            'password': '123456',
            'name': 'testcase',
            # 'is_staff': True,
            # 'is_superuser': True
        }
        # self.expdate = datetime.datetime(2040, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)

        self.user = get_user_model().objects.create(**user_payload)
        # token = Token.objects.get(user__name='testcase')
        
        # self.client.credentials(HTTP_AUTHORIZATION='Token AB7JSH^4454')
        # self.token = self.user.oauth2_provider_accesstoken.create(expires=self.expdate, token='1234567890')

        # self.client.credentials(Authorization='Bearer {}'.format(self.token))
        self.client.force_authenticate(self.user)
        
    def test_get_user_urls(self):
        """Test get user urls"""
        url = reverse('user:user-list')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        