from django.test import TestCase, Client
from django.urls import reverse
from ..models import Event

class TestViews(TestCase):

    def setUp(self):
        Event.objects.create(title="Test", slug="test")

    def test_event_view_GET(self):
        client = Client()
        event = Event.objects.get(slug="test")
        response = client.get(reverse('event', args=[event.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event.html')

