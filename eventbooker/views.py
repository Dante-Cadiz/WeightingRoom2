from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
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

        return render(
            request, "event.html", 
            {
                "event": event,
                "attendees": attendees
            },)

#class Attendance(View):
# used for logging the user's attendance/modifying db model with Event.attendees.remove or Event.attendees.add, user based
# In template show number incrementing
# Some logic to prevent attending a fully booked event/show if an event is fully booked

