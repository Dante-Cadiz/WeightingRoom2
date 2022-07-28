from django.test import TestCase
from ..models import Event

class TestModels(TestCase):

    def setUp(self):
        event = Event.objects.create(title="Test")
        for i in range(5):
            event.attendees.create(username=f"testuser{i}")
        
    def test_string_method(self):
        event = Event.objects.get(title="Test")
        self.assertEqual(str(event), "Test")
    
    def test_attendees_method(self):
        event = Event.objects.get(title="Test")
        self.assertEqual(event.number_of_attendees(), 5)

