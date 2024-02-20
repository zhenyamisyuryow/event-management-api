from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Event, Attendee

class EventViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@test.com', password='testpass')
        self.token = RefreshToken.for_user(self.user)
        self.event = Event.objects.create(title='Test Event', location='Test Location', date=timezone.now(), organizer=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')

    def test_list_events(self):
        response = self.client.get(reverse('event-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_event(self):
        response = self.client.get(reverse('event-detail', kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Event')

    def test_list_created_events(self):
        response = self.client.get(reverse('event-list-created-events'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Event')

    def test_list_subscribed_events(self):
        # Subscribe user to the event
        Attendee.objects.create(event=self.event, user=self.user)
        response = self.client.get(reverse('event-list-subscribed-events'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Event')
