from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction
import logging

from .models import FlightBooking, ContactMessage

logger = logging.getLogger(__name__)


def home(request):
    return render(request, "home.html")


def flights(request):
    flights_list = []

    origin = request.GET.get("origin")
    destination = request.GET.get("destination")

    if origin and destination:
        flights_list = [
            {
                "airline": "EgyptAir",
                "origin": origin,
                "destination": destination,
                "departure": "08:30",
                "arrival": "12:10",
                "duration": "3h 40m",
                "price": "420",
            },
            {
                "airline": "Qatar Airways",
                "origin": origin,
                "destination": destination,
                "departure": "14:00",
                "arrival": "18:10",
                "duration": "4h 10m",
                "price": "460",
            },
            {
                "airline": "Turkish Airlines",
                "origin": origin,
                "destination": destination,
                "departure": "20:15",
                "arrival": "23:40",
                "duration": "3h 25m",
                "price": "410",
            },
        ]

    return render(
        request,
        "flights.html",
        {
            "flights": flights_list,
        },
    )


def hotels(request):
    return render(request, "hotels.html")


def students(request):
    return render(request, "students.html")


def medical(request):
    return render(request, "medical.html")


def request_quote(request):
    return render(request, "request_quote.html")

def contact(request):

    if request.method == "POST":

        ContactMessage.objects.create(
            name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            subject="Website Contact",
            message=request.POST.get("message"),
        )

        messages.success(
            request,
            "Thank you! Your message has been received."
        )

    return render(request, "contact.html")


@transaction.atomic
def book_flight(request):
    origin = request.GET.get("origin", "")
    destination = request.GET.get("destination", "")

    if request.method != "POST":
        return render(
            request,
            "booking_form.html",
            {
                "origin": origin,
                "destination": destination,
            },
        )

    booking = FlightBooking.objects.create(
        first_name=request.POST.get("first_name", "").strip(),
        last_name=request.POST.get("last_name", "").strip(),
        email=request.POST.get("email", "").strip(),
        phone=request.POST.get("phone", "").strip(),
        origin=request.POST.get("origin", "").strip(),
        destination=request.POST.get("destination", "").strip(),
        departure_date=request.POST.get("departure_date") or None,
        return_date=request.POST.get("return_date") or None,
        travel_class=request.POST.get("travel_class", ""),
        adults=int(request.POST.get("adults", 1)),
        children=int(request.POST.get("children", 0)),
        infants=int(request.POST.get("infants", 0)),
        special_request=request.POST.get("special_request", ""),
    )

    try:
        customer_message = f"""
Dear {booking.first_name} {booking.last_name},

Thank you for choosing Kalsi Global Links.

========================================
BOOKING CONFIRMATION
========================================

Booking Reference:
{booking.booking_reference}

Route:
{booking.origin} ➜ {booking.destination}

Departure:
{booking.departure_date}

Return:
{booking.return_date}

Passengers

Adults: {booking.adults}
Children: {booking.children}
Infants: {booking.infants}

Travel Class:
{booking.travel_class}

========================================

Our ticketing department is already reviewing your request.

One of our travel consultants will contact you shortly with the best available itinerary and pricing.

Thank you for trusting Kalsi Global Links.

www.kalsiglobal.com
"""

        send_mail(
            subject=f"KGL Booking Confirmation - {booking.booking_reference}",
            message=customer_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[booking.email],
            fail_silently=False,
        )

        admin_message = f"""
NEW BOOKING RECEIVED

Reference:
{booking.booking_reference}

Passenger:
{booking.first_name} {booking.last_name}

Email:
{booking.email}

Phone:
{booking.phone}

Route:
{booking.origin} ➜ {booking.destination}

Departure:
{booking.departure_date}

Return:
{booking.return_date}

Adults:
{booking.adults}

Children:
{booking.children}

Infants:
{booking.infants}

Travel Class:
{booking.travel_class}

Special Request:

{booking.special_request}
"""

        send_mail(
            subject=f"NEW BOOKING - {booking.booking_reference}",
            message=admin_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["tickets@kalsiglobal.com"],
            fail_silently=False,
        )

    except Exception as e:
        logger.exception("Email sending failed: %s", e)
        messages.warning(
            request,
            "Booking saved successfully, but the confirmation email could not be sent."
        )

    return render(
        request,
        "booking_success.html",
        {
            "booking": booking,
        },
    )