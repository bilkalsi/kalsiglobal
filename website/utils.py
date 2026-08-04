from django.core.mail import send_mail
from django.conf import settings


def send_contact_notification(contact):

    subject = f"New Contact Message: {contact.subject}"

    message = f"""
A new contact request has been received.

Name:
{contact.name}

Email:
{contact.email}

Phone:
{contact.phone}

Subject:
{contact.subject}

Message:
{contact.message}
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=True,
    )