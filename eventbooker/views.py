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
        user_attending = False
        for timeslot in timeslots:
            if timeslot.attendees.filter(id=self.request.user.id).exists():
                user_attending = True
        
        return render(
            request, "event.html", 
            {
                "event": event,
                "timeslots": timeslots,
                "user_attending": user_attending,
            },)

#class TimeslotView(View):
    #def get(self, request, slug, *args, **kwargs):
        
    #set the queryset to all upcoming timeslots
    #then narrow queryset to all upcoming timeslots that have a foreign key of the selected event
    #page displays list of all these timeslots looped in a for loop
    #get selected event somehow  - by slug? th getobjector404 method


class TimeslotAttendance(UpcomingEventMixin, View):
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        #timeslots = event.times.all()
        #if event.attendees.filter(id=request.user.id).exists():
            #event.attendees.remove(request.user)
       # else:
           # event.attendees.add(request.user)
        return HttpResponseRedirect(reverse('event', args=[slug]))
        

#class BookingView
#get user bookings by requesting user through link to bookings model
# display time/event
# add POST functionality to edit booking