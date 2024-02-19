from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'organizer']