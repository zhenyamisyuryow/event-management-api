from rest_framework import serializers
from .models import Event

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