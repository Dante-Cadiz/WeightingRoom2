from django.contrib import admin
from .models import Event, EventTimeslot
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class TimeslotInline(admin.TabularInline):
    model = EventTimeslot
    exclude = ['user_attending',]

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    inlines = [TimeslotInline, ]

