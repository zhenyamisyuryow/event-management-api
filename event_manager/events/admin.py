from django.contrib import admin
from .models import Event
from django.contrib.admin import ModelAdmin

class EventAdmin(ModelAdmin):
    list_display = ['title', 'date', 'location', 'organizer']
    search_fields = ['title', 'location', 'organizer__email']
    list_filter = ['date', 'location', 'organizer__email']

admin.site.register(Event, EventAdmin)