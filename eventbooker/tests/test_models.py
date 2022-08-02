from django.test import TestCase
from ..models import Event, Timeslot, Booking
from datetime import datetime

class TestEventModel(TestCase):

    def setUp(self):
        event = Event.objects.create(title="Test")
        Timeslot.objects.create(time=datetime(2022, 8, 20, 15, 30), event=Event.objects.get(title="Test"))
        for i in range(5):
            event.attendees.create(username=f"testuser{i}")
        
    def test_string_method(self):
        event = Event.objects.get(title="Test")
        self.assertEqual(str(event), "Test")
    
    def test_attendees_method(self):
        event = Event.objects.get(title="Test")
        self.assertEqual(event.number_of_attendees(), 5)
    
    def test_timeslot_strftime(self):
        timeslot = Timeslot.objects.get(event=Event.objects.get(title="Test"))
        self.assertEqual(timeslot.show_timeslots(), '20/8, 15:30')

    

