from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm
from .utils import send_contact_notification


def home(request):
    return render(request, "website/home.html")


def about(request):
    return render(request, "website/about.html")


def services(request):
    return render(request, "website/services.html")


def flights(request):
    return render(request, "website/flights.html")


def hotels(request):
    return render(request, "website/hotels.html")


def students(request):
    return render(request, "website/students.html")


def medical(request):
    return render(request, "website/medical.html")


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            contact = form.save()

            send_contact_notification(contact)

            messages.success(
                request,
                "Your message has been sent successfully.",
            )

            return redirect("website:contact")

    else:

        form = ContactForm()

    return render(
        request,
        "website/contact.html",
        {
            "form": form,
        },
    )


def page_not_found(request, exception):
    return render(request, "website/404.html", status=404)


def server_error(request):
    return render(request, "website/500.html", status=500)