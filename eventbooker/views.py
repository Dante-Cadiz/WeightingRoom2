from django.shortcuts import render
from django.views import generic, View
from .models import Event


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by("scheduled_time")
    template_name = "index.html"

#class EventView(View):

    # show whether the currently logged in user is attending based on the many to many relationship value by setting 'attending' variable
    # 


#class Attendance(View):
# used for logging the user's attendance/modifying db model with Event.attendees.remove or Event.attendees.add, user based
# In template show number incrementing
# Some logic to prevent attending a fully booked event/show if an event is fully booked

