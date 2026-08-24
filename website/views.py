from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import (
    ContactForm,
    FlightRequestForm,
    HotelRequestForm,
    MedicalRequestForm,
    NewsletterForm,
    StudentRequestForm,
)


def home(request):
    return render(request, "website/home.html")


def about(request):
    return render(request, "website/about.html")


def services(request):
    return render(request, "website/services.html")


def flights(request):
    if request.method == "POST":
        form = FlightRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your flight request has been submitted successfully.")
            return redirect("website:flights")
    else:
        form = FlightRequestForm()

    return render(request, "website/flights.html", {"form": form})


def hotels(request):
    if request.method == "POST":
        form = HotelRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your hotel request has been submitted successfully.")
            return redirect("website:hotels")
    else:
        form = HotelRequestForm()

    return render(request, "website/hotels.html", {"form": form})


def students(request):
    if request.method == "POST":
        form = StudentRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your study enquiry has been submitted successfully.")
            return redirect("website:students")
    else:
        form = StudentRequestForm()

    return render(request, "website/students.html", {"form": form})


def medical(request):
    if request.method == "POST":
        form = MedicalRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your medical enquiry has been submitted successfully.")
            return redirect("website:medical")
    else:
        form = MedicalRequestForm()

    return render(request, "website/medical.html", {"form": form})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you. We have received your enquiry and will contact you shortly."
            )
            return redirect("website:contact")
    else:
        form = ContactForm()

    return render(request, "website/contact.html", {"form": form})


def subscribe(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing.")

    return redirect(request.META.get("HTTP_REFERER", "website:home"))

from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, "website/404.html", status=404)


def server_error(request):
    return render(request, "website/500.html", status=500)