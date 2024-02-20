from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import Attendee


# Signal to send email to user after successful registration. Django console backend is used in development
@receiver(post_save, sender=Attendee)
def send_email(sender, instance, created, **kwargs):
    if created:
        event_title = instance.event.title
        event_date = instance.event.date
        location = instance.event.location
        try:
            send_mail(
                subject = f'You have successfully registered for {event_title}',
                message = f'''Thank you for registering for the event. 
                The event will take place on {event_date}.
                Event location: {location}''',
                from_email= settings.EMAIL_HOST_USER,
                recipient_list=[instance.user.email],
                fail_silently=False,
            )
            instance.initial_notification_sent = True
            instance.save()
            return True
        except:
            return False