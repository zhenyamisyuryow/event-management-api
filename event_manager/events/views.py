from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Event, Attendee
from .serializers import EventSerializer, AttendeeSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'location', 'organizer__email', 'date']
    ordering_fields = ['date', 'location', 'organizer', 'title']

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Event.objects.all()
        return Event.objects.filter(organizer=self.request.user)
    
    # Custom action to list events organized by the user
    @action(detail=False, methods=['GET'])
    def list_created_events(self, request):
        events = Event.objects.filter(organizer=request.user)
        if not events.exists():
            return Response({'message': 'You have no events.'}, status=200)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def list_subscribed_events(self, request):
        events = Event.objects.filter(attendees__user=request.user)
        if not events.exists():
            return Response({'message': 'You have not registered for any event.'}, status=200)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
    

class EventSubscribe(CreateAPIView):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventUnsubscribe(DestroyAPIView):
    serializer_class = AttendeeSerializer

    def get_queryset(self):
        return Attendee.objects.filter(user=self.request.user)

    def destroy(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        event_id = serializer.validated_data.get('event')
        attendee = self.get_queryset().filter(event=event_id).first()

        if attendee:
            self.perform_destroy(attendee)
            return Response({'message': 'You have successfully unregistered from the event.'}, status=200)
        return Response({'message': 'You are not registered for this event.'}, status=400)