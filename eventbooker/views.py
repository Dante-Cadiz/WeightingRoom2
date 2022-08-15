from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event, EventTimeslot, Booking


#restructure CBVs making a context mixin that covers all context
class UpcomingEventMixin(object):
    queryset = Event.objects.filter(status=1) 

#class AttendanceMixin(object):

class EventList(UpcomingEventMixin, generic.ListView):
    template_name = "index.html"

class EventView(UpcomingEventMixin, View):
    def get(self, request, slug, *args, **kwargs):
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        timeslots = EventTimeslot.objects.filter(event=event).order_by('start_time')
        
        return render(
            request, "event.html", 
            {
                "event": event,
                "timeslots": timeslots,
            },)

#class TimeslotView(View):
    #def get(self, request, slug, *args, **kwargs):
        
    # can use the same method as in the post request to get the individual timeslots, with a boolean value as to whether the user is attending them?
    # where is this returned to
    # maybe have this as a timeslot content mixin?

class TimeslotAttendance(UpcomingEventMixin, View):

    def get(self, request, slug, *args, **kwargs):
        timeslots = EventTimeslot.objects.all()
        timeslot = get_object_or_404(timeslots, id=self.kwargs['pk'])
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        if timeslot.event != event: 
            raise ValueError('Timeslot must relate to event')
        user_attending = False
        if timeslot.attendees.filter(id=request.user.id).exists():
            user_attending = True

        return HttpResponseRedirect(reverse('event', args=[slug]))
    
    def post(self, request, slug, *args, **kwargs):
        timeslots = EventTimeslot.objects.all()
        timeslot = get_object_or_404(timeslots, id=self.kwargs['pk'])
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        if timeslot.event != event: 
            raise ValueError('Timeslot must relate to event')

        if timeslot.attendees.filter(id=request.user.id).exists():
            timeslot.attendees.remove(request.user)
        else:
            timeslot.attendees.add(request.user)
        return HttpResponseRedirect(reverse('event', args=[slug]))
        

class BookingsView(View):

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(booker=self.request.user.id).order_by('timeslot')
        return render(
            request, "my_bookings.html", 
            {
                "bookings": bookings,
            },)
    
