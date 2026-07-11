from django.contrib import admin
from .models import FlightBooking, ContactMessage


@admin.register(FlightBooking)
class FlightBookingAdmin(admin.ModelAdmin):
    list_display = (
        "booking_reference",
        "first_name",
        "last_name",
        "origin",
        "destination",
        "departure_date",
        "status",
        "created_at",
    )

    search_fields = (
        "booking_reference",
        "first_name",
        "last_name",
        "email",
        "phone",
        "origin",
        "destination",
    )

    list_filter = (
        "status",
        "departure_date",
        "created_at",
    )

    readonly_fields = (
        "booking_reference",
        "created_at",
    )

    ordering = ("-created_at",)

    list_per_page = 20


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = ("-created_at",)