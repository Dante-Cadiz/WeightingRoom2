from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event, EventTimeslot


#restructure CBVs making a context mixin that covers all context
class UpcomingEventMixin(object):
    queryset = Event.objects.filter(status=1) 

#class AttendanceMixin(object):

class EventList(UpcomingEventMixin, generic.ListView):
    template_name = "index.html"

class EventView(UpcomingEventMixin, View):
    def get(self, request, slug, *args, **kwargs):
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        timeslots = event.times.all().order_by("start_time")
        
        return render(
            request, "event.html", 
            {
                "event": event,
                "timeslots": timeslots,
            },)

#class TimeslotView(View):
    #def get(self, request, slug, *args, **kwargs):
        
    #set the queryset to all upcoming timeslots
    #then narrow queryset to all upcoming timeslots that have a foreign key of the selected event
    #page displays list of all these timeslots looped in a for loop
    #get selected event somehow  - by slug? th getobjector404 method


class TimeslotAttendance(UpcomingEventMixin, View):
    def post(self, request, slug, *args, **kwargs):
        #fetch the Event and validate that that timeslot does actually belong to that event
        timeslots = EventTimeslot.objects.all()
        timeslot = get_object_or_404(timeslots, id=id)
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        if timeslot.event != event: 
            raise ValueError('Timeslot must relate to event')
        #timeslot = another get_object_or_404 on the timeslot based on its ID
        #for timeslot in timeslots no for loop
        if timeslot.attendees.filter(id=request.user.id).exists():
            timeslot.attendees.remove(request.user)
        else:
            timeslot.attendees.add(request.user)
        return HttpResponseRedirect(reverse('event', args=[slug])) #change reverse to return something with the timeslot
        

#class BookingView
#get user bookings by requesting user through link to bookings model
# display time/event
# add POST functionality to edit booking