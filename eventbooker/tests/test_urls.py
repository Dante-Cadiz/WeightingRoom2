from django.test import TestCase
from ..models import Event

class TestUrls(TestCase):
    
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'index.html')
    
    #def test_event_page(self):
        #response = self.client.get('/test')
        #self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, 'event.html')