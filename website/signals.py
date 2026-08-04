from django.db.models.signals import post_save
from django.dispatch import receiver

from website.models import ContactMessage


@receiver(post_save, sender=ContactMessage)
def contact_message_created(sender, instance, created, **kwargs):
    if created:
        pass