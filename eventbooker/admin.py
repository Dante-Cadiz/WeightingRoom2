from django.contrib import admin
from .models import Event, EventTimeslot, Booking, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class TimeslotInline(admin.TabularInline):
    model = EventTimeslot

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    inlines = [TimeslotInline, ]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)