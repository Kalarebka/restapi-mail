from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse

from .models import Mailbox, Template, Email


class MailboxTests(APITestCase):
    def test_create_mailbox(self):
        """ Test creating a new mailbox"""
        url = reverse('mailbox_list')
        data = {'host': 'host address',
                'port': 25,
                'login': 'user_login',
                'password': 'user_password',
                'email_from': 'sender',
                'use_ssl': True,
                'is_active': True,
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mailbox.objects.count(), 1)
        self.assertEqual(Mailbox.objects.get().login, 'user_login')
