from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event, Timeslot


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
        #figure out how to access an individual timeslot, while knowing which one you are going to access
        #iterating across for loop?
        #figure out how to make this block of logic work with respect to the timeslots
        attendees = timeslot.number_of_attendees()
        user_attending = False
        if timeslot.attendees.filter(id=self.request.user.id).exists():
            user_attending = True
        

        return render(
            request, "event.html", 
            {
                "event": event,
                "attendees": attendees,
                "user_attending": user_attending,
                "timeslots": timeslots
            },)

class EventAttendance(UpcomingEventMixin, View):
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        timeslots = event.times.all().order_by("start_time")
        # figure out how to make this block of logic apply
        if timeslot.attendees.filter(id=request.user.id).exists():
            timeslot.attendees.remove(request.user)
        else:
            timeslot.attendees.add(request.user)

        return HttpResponseRedirect(reverse('event', args=[slug]))
        
#class TimeslotView

#or user events as view for myevents.html page
#if event.attendees(id=request.user.id).exists()
# event.attendees.add(request.user)  else, etd
