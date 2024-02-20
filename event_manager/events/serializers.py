from rest_framework import serializers

from django.db import IntegrityError

from .models import Event, Attendee

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'organizer']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Event.objects.all(),
                fields=['title', 'date', 'location'],
                message='You can only host one event with the same title, date, and location.'
            )
        ]
    
    def create(self, validated_data):
        event = Event.objects.create(**validated_data, organizer=self.context['request'].user)
        return event
    
class AttendeeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), required=True)

    class Meta:
        model = Attendee
        fields = ['event', 'user']
        
    def create(self, validated_data):
        try:
            attendee = Attendee.objects.create(**validated_data)
            return attendee
        except IntegrityError:
            raise serializers.ValidationError({"error": "You are already registered for this event."})
    