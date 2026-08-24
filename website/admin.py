from django.contrib import admin

admin.site.site_header = "Kalsi Global Links Administration"
admin.site.site_title = "Kalsi Global Links"
admin.site.index_title = "Management Dashboard"

from .models import (
    ContactMessage,
    FlightRequest,
    HotelRequest,
    StudentRequest,
    MedicalRequest,
    NewsletterSubscriber,
)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "subject", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("created_at",)


@admin.register(FlightRequest)
class FlightRequestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "origin",
        "destination",
        "departure_date",
        "created_at",
    )
    search_fields = ("name", "email", "origin", "destination")
    list_filter = ("travel_class", "created_at")


@admin.register(HotelRequest)
class HotelRequestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "destination",
        "check_in",
        "check_out",
        "created_at",
    )
    search_fields = ("name", "email", "destination")
    list_filter = ("hotel_standard", "created_at")


@admin.register(StudentRequest)
class StudentRequestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "study_level",
        "destination",
        "created_at",
    )
    search_fields = ("name", "email", "destination")
    list_filter = ("study_level", "created_at")


@admin.register(MedicalRequest)
class MedicalRequestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "destination",
        "treatment",
        "created_at",
    )
    search_fields = ("name", "email", "destination")
    list_filter = ("created_at",)


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email",)