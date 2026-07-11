from django.urls import path

from . import views

## app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),

    # Flights
    path("flights/", views.flights, name="flights"),
    path("book-flight/", views.book_flight, name="book_flight"),

    # Hotels
    path("hotels/", views.hotels, name="hotels"),

    # Study Abroad
    path("students/", views.students, name="students"),

    # Medical Tourism
    path("medical/", views.medical, name="medical"),

    # Quote Request
    path("request-quote/", views.request_quote, name="request_quote"),

    # Contact
    path("contact/", views.contact, name="contact"),
]