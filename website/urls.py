from django.urls import path

from . import views

app_name = "website"

urlpatterns = [

    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "about/",
        views.about,
        name="about",
    ),

    path(
        "services/",
        views.services,
        name="services",
    ),

    path(
        "flights/",
        views.flights,
        name="flights",
    ),

    path(
        "hotels/",
        views.hotels,
        name="hotels",
    ),

    path(
        "students/",
        views.students,
        name="students",
    ),

    path(
        "medical/",
        views.medical,
        name="medical",
    ),

    path(
        "contact/",
        views.contact,
        name="contact",
    ),

]