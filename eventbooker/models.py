from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Upcoming'), (2, 'Past'))
now = timezone.now()

#make events automatically become past events after the time has passed

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.RESTRICT,
                               related_name="events", null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    max_attendees = models.IntegerField(null=True)

    def __str__(self):
        return self.title
    
    
    #get_absolute_url method?
    
    
class EventTimeslot(models.Model):
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name='times', null=True)
    attendees = models.ManyToManyField(User, blank=True)
                                       
    def number_of_attendees(self):
        return self.attendees.count()
    
    def set_to_past(self):
        if self.start_time < now:
            self.event.status = 2
    
    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("Start time must be before end time.")

    def __str__(self):
        return f"{str(self.start_time)} - {str(self.end_time)}"
          

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, 
                              related_name='event', blank=True)
    booker = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name='booker', blank=True)
    timeslot = models.ForeignKey(EventTimeslot, on_delete=models.CASCADE, 
                                 related_name='timeslots', blank=True)
    
    #get_absolute_url method?

# maybe redesign entire thing with booking.create view 

