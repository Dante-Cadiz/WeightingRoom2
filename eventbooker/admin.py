from django.contrib import admin
from .models import Event, Timeslot
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class TimeslotInline(admin.TabularInline):
    model = Timeslot


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    exclude = ('timeslots',)
    inlines = [TimeslotInline, ]

