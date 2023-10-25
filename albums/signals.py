from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Album
from .tasks import send_congratulatory_email
from django.utils import timezone


@receiver(post_save, sender=Album)
def send_congrates_email_signal(sender, instance, created, **kwargs):
    if created:
        instance.release_datetime = timezone.now()
        instance.save()
        send_congratulatory_email.delay(
            instance.artist.user.username, instance.artist.user.email, instance.name
        )
