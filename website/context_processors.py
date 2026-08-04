from django.conf import settings


def site_settings(request):
    return {
        "SITE_NAME": "Kalsi Global Links",
        "SITE_URL": "https://kalsiglobal.com",
        "SITE_EMAIL": "info@kalsiglobal.com",
        "SITE_PHONE": "+54 9 249 467336",
        "COPYRIGHT_YEAR": 2023,
        "DEBUG": settings.DEBUG,
    }