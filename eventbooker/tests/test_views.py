from django.test import TestCase, Client
from django.urls import reverse
from ..models import Event, EventTimeslot, Booking
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        event = Event.objects.create(title="Test", slug='test')
        

    def test_event_view_GET(self):
        event = Event.objects.get(slug="test")
        response = self.client.get(reverse('event', args=[event.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event.html')

        self.assertContains(response.content, "<h2 class=\"card-title my-2\">Test</h2>")

