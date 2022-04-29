from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class IndexTest(TestCase):
    def Set_up(self):
        client = Client()
        self.response = client.get(reverse('index'))

    def main_responce(self):
        self.assertEqual(self.response.status_code, 200)

    def main_contest(self):
        self.assertEqual(self.response.context[])

class CrosswordTestCase(TestCase):

