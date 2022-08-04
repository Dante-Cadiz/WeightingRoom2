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
        
        return render(
            request, "event.html", 
            {
                "event": event,
            },)

class EventAttendance(UpcomingEventMixin, View):
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        
        return HttpResponseRedirect(reverse('event', args=[slug]))
        
#class TimeslotView

#or user events as view for myevents.html page
#if event.attendees(id=request.user.id).exists()
# event.attendees.add(request.user)  else, etd
