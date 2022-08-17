from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event, EventTimeslot, Booking


class UpcomingEventMixin(object):
    queryset = Event.objects.filter(status=1) 

class EventList(UpcomingEventMixin, generic.ListView):
    template_name = "index.html"

class EventView(UpcomingEventMixin, View):
    def get(self, request, slug, *args, **kwargs):
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        timeslots = EventTimeslot.objects.filter(event=event).order_by(
                     'start_time').exclude(attendees=self.request.user)
        bookings = Booking.objects.filter(event=event, 
                                          booker=self.request.user)
        
        return render(
            request, "event.html", 
            {
                "event": event,
                "timeslots": timeslots,
                "bookings": bookings,
            },)


class TimeslotAttendance(UpcomingEventMixin, View):
    
    def post(self, request, slug, *args, **kwargs):
        timeslots = EventTimeslot.objects.all()
        timeslot = get_object_or_404(timeslots, id=self.kwargs['pk'])
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        if timeslot.event != event: 
            raise ValueError('Timeslot must relate to event')

        if timeslot.attendees.filter(id=request.user.id).exists():
            timeslot.attendees.remove(request.user)
            Booking.objects.filter(event=event, booker=self.request.user, 
                                   timeslot=timeslot).delete()
        else:
            timeslot.attendees.add(request.user)
            Booking.objects.create(event=event, booker=self.request.user, timeslot=timeslot)
        return HttpResponseRedirect(reverse('event', args=[slug]))


class BookingsView(View):

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(booker=self.request.user.id).order_by('timeslot')
        return render(
            request, "my_bookings.html", 
            {
                "bookings": bookings,
            },)
    
