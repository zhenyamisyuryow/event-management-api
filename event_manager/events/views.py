from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Event
from .serializers import EventSerializer

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def perform_create(self, serializer):
        return serializer.save(organizer=self.request.user)