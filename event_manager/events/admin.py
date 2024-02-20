from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Event, Attendee

class EventAdmin(ModelAdmin):
    list_display = ['title', 'date', 'location', 'organizer']
    search_fields = ['title', 'location', 'organizer__email']
    list_filter = ['date', 'location', 'organizer__email']

admin.site.register(Event, EventAdmin)

class AttendeeAdmin(ModelAdmin):
    list_display = ['event', 'user', 'initial_notification_sent']
    search_fields = ['event__title', 'user__email']
    list_filter = ['event__title', 'user__email']

admin.site.register(Attendee, AttendeeAdmin)