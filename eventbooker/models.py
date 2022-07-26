from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Upcoming'), (2, 'Past'))

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="events", null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.DateTimeField(null=True)
    attendees = models.ManyToManyField(User, related_name='attending_user', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
    
    def number_of_attendees(self):
        return self.attendees.count()

#class EventBooking(models.Model):
    #user = models.ForeignKey(User, related)
    # some specific logic that allows the user to access their own list of events depending on who they are

# or -- class SiteUser - subclass/extension of User class which has many to many field for events
# can easily add/edit events they are attending that way