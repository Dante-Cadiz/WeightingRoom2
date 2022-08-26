from django.test import TestCase
from ..models import Event
from django.urls import reverse, resolve
from ..views import EventView, BookingsView, MakeBooking, CancelBooking

class TestUrls(TestCase):
    
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'index.html')
    
    def test_event_detail_url_resolves(self):
        url = reverse('event', args=['test_slug'])
        self.assertEqual(resolve(url).func.view_class, EventView)
    
    def test_my_bookings_url_resolves(self):
        url = reverse('my_bookings')
        self.assertEqual(resolve(url).func.view_class, BookingsView)
    
    def test_make_booking_url_resolves(self):
        url = reverse('make_booking', args=['test_slug', 1])
        self.assertEqual(resolve(url).func.view_class, MakeBooking)
    
    def test_cancel_booking_url_resolves(self):
        url = reverse('cancel_booking', args=['test_slug', 1])
        self.assertEqual(resolve(url).func.view_class, CancelBooking)

    

    
