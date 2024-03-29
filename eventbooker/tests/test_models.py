from django.test import TestCase
from ..models import Event, EventTimeslot, Booking
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

class TestAllModels(TestCase):

    def setUp(self):
        user = User.objects.create(id=1)
        event = Event.objects.create(title="Test")
        timeslot = EventTimeslot.objects.create(id=1, start_time=datetime(2022, 8, 20, 15, 30),
            end_time=datetime(2022, 8, 20, 16, 30), event=Event.objects.get(title="Test"))
        booking = Booking.objects.create(id=1, event=event, booker=user, timeslot=timeslot)
        EventTimeslot.objects.create(id=2, start_time=datetime(2022, 8, 20, 15, 30),
            end_time=datetime(2022, 8, 20, 14, 30), event=Event.objects.get(title="Test"))
        for i in range(5):
            timeslot.attendees.create(username=f"testuser{i}")
        
    def test_event_string_representation(self):
        event = Event.objects.get(title="Test")
        self.assertEqual(str(event), "Test")
    
    def test_attendees_counted_correctly(self):
        timeslot = EventTimeslot.objects.get(id=1)
        self.assertEqual(timeslot.number_of_attendees(), 5)
    
    def test_time_validation(self):
        timeslot2 = EventTimeslot.objects.get(id=2)
        # TODO: Verify the exact error message.
        with self.assertRaises(ValidationError):
            timeslot2.clean()
    
    def test_timeslot_updates_status(self):
        timeslot = EventTimeslot.objects.get(id=1)
        timeslot.set_to_past()
        self.assertEqual(timeslot.event.status, 2)

    def test_timeslot_representation(self):
        timeslot = EventTimeslot.objects.get(id=1)
        self.assertEqual(str(timeslot), '20/8, 15:30 - 16:30')
    
    def test_booking_representation(self):
        booking = Booking.objects.get(id=1)
        self.assertEqual(str(booking), "20/8, 15:30 - 16:30")

    

