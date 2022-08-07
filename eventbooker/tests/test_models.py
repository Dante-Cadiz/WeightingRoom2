from django.test import TestCase
from ..models import Event, EventTimeslot, Booking
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
    
    def test_status_update_method(self):
        timeslot = EventTimeslot.objects.get(event=Event.objects.get(title="Test"))
        timeslot.start_time=datetime(2021, 8, 20, 16, 30)
        self.assertEqual(timeslot.event.status, 5)
    


    #create test that tests the clean() method, have to figure out how to access individual timeslots first

    def test_timeslot_strftime(self):
        timeslot = EventTimeslot.objects.get(event=Event.objects.get(title="Test"))
        self.assertEqual(timeslot.show_timeslots(), '20/8, 15:30 - 16:30')

    

