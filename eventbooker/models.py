from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Upcoming'), (2, 'Past'))

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.RESTRICT,
                               related_name="events", null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    timeslots = models.ForeignKey('Timeslot', on_delete=models.RESTRICT,
                                  related_name='times', null=True)
    attendees = models.ManyToManyField(User, related_name='attending_user',
                                       blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    max_attendees = models.IntegerField(null=True)

    def __str__(self):
        return self.title
    
    def number_of_attendees(self):
        return self.attendees.count()
    
    def show_timeslots(self):
        #figure out how to get an iterable value out of the timeslots
        #for time in times:
           # return time.strftime("%m/%d, %H:%M")

class Timeslot(models.Model):
    time = models.DateTimeField(null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name='associated_event', null=True)

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, 
                              related_name='event', blank=True)
    booker = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name='booker', blank=True)
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE, 
                                 related_name='timeslots', blank=True)

