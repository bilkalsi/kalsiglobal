from django.db import models


class BaseRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ContactMessage(BaseRequest):
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FlightRequest(BaseRequest):
    trip_type = models.CharField(max_length=20)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    passengers = models.PositiveIntegerField(default=1)
    travel_class = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} - {self.origin} → {self.destination}"


class HotelRequest(BaseRequest):
    destination = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(default=1)
    rooms = models.PositiveIntegerField(default=1)
    hotel_standard = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} - {self.destination}"


class StudentRequest(BaseRequest):
    country = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    study_level = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MedicalRequest(BaseRequest):
    country = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    treatment = models.CharField(max_length=200)
    travelers = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email