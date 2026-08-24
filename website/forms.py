from django import forms

from .models import (
    ContactMessage,
    FlightRequest,
    HotelRequest,
    StudentRequest,
    MedicalRequest,
    NewsletterSubscriber,
)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            "name",
            "email",
            "phone",
            "subject",
            "message",
        ]


class FlightRequestForm(forms.ModelForm):
    class Meta:
        model = FlightRequest
        fields = "__all__"

        widgets = {
            "departure_date": forms.DateInput(attrs={"type": "date"}),
            "return_date": forms.DateInput(attrs={"type": "date"}),
        }


class HotelRequestForm(forms.ModelForm):
    class Meta:
        model = HotelRequest
        fields = "__all__"

        widgets = {
            "check_in": forms.DateInput(attrs={"type": "date"}),
            "check_out": forms.DateInput(attrs={"type": "date"}),
        }


class StudentRequestForm(forms.ModelForm):
    class Meta:
        model = StudentRequest
        fields = "__all__"


class MedicalRequestForm(forms.ModelForm):
    class Meta:
        model = MedicalRequest
        fields = "__all__"


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ["email"]