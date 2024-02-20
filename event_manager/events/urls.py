from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import EventViewSet, EventSubscribe, EventUnsubscribe

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('events/subscribe', EventSubscribe.as_view(), name="event-subscribe"),
    path('events/unsubscribe', EventUnsubscribe.as_view(), name="event-subscribe"),
    path('', include(router.urls)),
]
