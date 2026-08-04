from django.core.management.base import BaseCommand

from website.models import ContactMessage


class Command(BaseCommand):
    help = "Seed the database."

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.SUCCESS("Database seed completed successfully."))