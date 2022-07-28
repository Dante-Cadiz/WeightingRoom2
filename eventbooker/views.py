from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by("scheduled_time")
    template_name = "index.html"

class EventView(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        attendees = event.attendees
        user_attending = False
        if event.attendees.filter(username=self.request.user.username).exists():
            user_attending = True

        return render(
            request, "event.html", 
            {
                "event": event,
                "attendees": attendees,
                "user_attending": user_attending
            },)

class EventAttendance(View):
    def event(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)
        if event.attendees.filter(id=request.user.id).exists():
            event.attendees.remove(request.user)
        else:
            event.attendees.add(request.user)

        return HttpResponseRedirect(reverse('event', args=[slug]))
        #figure out why this httpresponseredirect isn't doing anything and is instead linking to some nonexistent 'booking' page



#or user events as view for myevents.html page
#if event.attendees(id=request.user.id).exists()
# event.attendees.add(request.user)  else, etd
