from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event, EventTimeslot, Booking
from .forms import CommentForm


class UpcomingEventMixin(object):
    queryset = Event.objects.filter(status=1) 

class EventList(UpcomingEventMixin, generic.ListView):
    template_name = "index.html"

class EventView(UpcomingEventMixin, View):
    def get(self, request, slug, *args, **kwargs):
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by("-created_on")
        if self.request.user.is_authenticated:
            timeslots = EventTimeslot.objects.filter(event=event).order_by(
                     'start_time').exclude(attendees=self.request.user)
            bookings = Booking.objects.filter(event=event, 
                                              booker=self.request.user)
        
            return render(
                request, "event.html", 
                {
                    "event": event,
                    "comments": comments,
                    "timeslots": timeslots,
                    "bookings": bookings,
                    "user_commented": False,
                    "comment_form": CommentForm()
                },)
        
        else:
            timeslots = EventTimeslot.objects.filter(event=event).order_by(
                     'start_time')
            
            return render(
                request, "event.html", 
                {
                    "event": event,
                    "comments": comments,
                    "timeslots": timeslots,
                },)
    
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by("-created_on")
        timeslots = EventTimeslot.objects.filter(event=event).order_by(
                     'start_time').exclude(attendees=self.request.user)
        bookings = Booking.objects.filter(event=event, 
                                        booker=self.request.user)
        
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render(
                request, "event.html", 
                {
                    "event": event,
                    "comments": comments,
                    "timeslots": timeslots,
                    "bookings": bookings,
                    "comment_form": comment_form,
                    "user_commented": True,
                },)

#class EditComment/DeleteComment()


class MakeBooking(UpcomingEventMixin, View):
    
    def post(self, request, slug, *args, **kwargs):
        timeslots = EventTimeslot.objects.all()
        timeslot = get_object_or_404(timeslots, id=self.kwargs['pk'])
        event = get_object_or_404(UpcomingEventMixin.queryset, slug=slug)
        if timeslot.event != event: 
            raise ValueError('Timeslot must relate to event')

        timeslot.attendees.add(request.user)
        Booking.objects.create(event=event, booker=self.request.user, timeslot=timeslot)
        return HttpResponseRedirect(reverse('event', args=[slug]))

class CancelBooking(UpcomingEventMixin, View):
    def post(self, request, slug, *args, **kwargs):
        bookings = Booking.objects.all()
        booking = get_object_or_404(bookings, id=self.kwargs['pk'])
        timeslot = booking.timeslot
        timeslot.attendees.remove(self.request.user)
        booking.delete()

        return HttpResponseRedirect(reverse('event', args=[slug]))



class BookingsView(View):

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(
                booker=self.request.user.id).order_by('timeslot')
        return render(
            request, "my_bookings.html", 
            {
                "bookings": bookings,
            },)
    
