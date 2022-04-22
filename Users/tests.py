from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


from Storage.models import BasicSettings

class IndexTest(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get(reverse('index'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_context(self):
        self.assertEqual(self.response.context['pages'], 3)
        self.assertEqual(self.response.context['auth'], 'Andrew')
        self.assertTrue('cr_date' in self.response.context)

class BasicSettingsTest(TestCase):
    fixtures = ['test_database.json']   # manage.py dumpdata to get it