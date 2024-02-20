from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Event
from .serializers import EventSerializer

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Event.objects.all()
        return Event.objects.filter(organizer=self.request.user)
    

    @action(detail=False, methods=['GET'])
    def list_my_events(self, request):
        events = Event.objects.filter(organizer=request.user)
        if not events.exists():
            return Response({'message': 'You have no events.'}, status=200)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)