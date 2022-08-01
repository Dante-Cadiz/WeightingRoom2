from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')