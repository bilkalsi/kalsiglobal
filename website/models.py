from django.db import models
import uuid


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"


class FlightBooking(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Ticketed", "Ticketed"),
        ("Cancelled", "Cancelled"),
    ]

    booking_reference = models.CharField(max_length=20, unique=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField()
    phone = models.CharField(max_length=50)

    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    departure_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    travel_class = models.CharField(max_length=50, blank=True)

    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    infants = models.PositiveIntegerField(default=0)

    special_request = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.booking_reference:
            while True:
                reference = f"KGL-{uuid.uuid4().hex[:6].upper()}"
                if not FlightBooking.objects.filter(
                    booking_reference=reference
                ).exists():
                    self.booking_reference = reference
                    break

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.booking_reference} | {self.first_name} {self.last_name}"