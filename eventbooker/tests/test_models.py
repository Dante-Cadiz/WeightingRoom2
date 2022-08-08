from django.test import TestCase
from ..models import Event, EventTimeslot, Booking
from django.core.exceptions import ValidationError
from datetime import datetime

class TestEventModel(TestCase):

    def setUp(self):
        event = Event.objects.create(title="Test")
        timeslot = EventTimeslot.objects.create(start_time=datetime(2022, 8, 20, 15, 30),
            end_time=datetime(2022, 8, 20, 16, 30), event=Event.objects.get(title="Test"))
        for i in range(5):
            timeslot.attendees.create(username=f"testuser{i}")
        
    def test_string_method(self):
        event = Event.objects.get(title="Test")
        self.assertEqual(str(event), "Test")
    
    def test_attendees_method(self):
        timeslot = EventTimeslot.objects.get(event=Event.objects.get(title="Test"))
        self.assertEqual(timeslot.number_of_attendees(), 5)
    
    def test_clean_method(self):
        timeslot = EventTimeslot.objects.get(event=Event.objects.get(title="Test"))
        timeslot.start_time=datetime(2021, 8, 20, 17, 30)
        with self.assertRaises(ValidationError):
            timeslot.clean()
    
    def test_status_update_method(self):
        timeslot = EventTimeslot.objects.get(event=Event.objects.get(title="Test"))
        timeslot.start_time=datetime(2021, 8, 20, 16, 30)
        timeslot.set_to_past()
        self.assertEqual(timeslot.event.status, 2)
    


    #create test that tests the clean() method, have to figure out how to access individual timeslots first

    def test_timeslot_string_method(self):
        timeslot = EventTimeslot.objects.get(event=Event.objects.get(title="Test"))
        self.assertEqual(str(timeslot), '20/8, 15:30 - 16:30')

    

