from .version import VERSION, BUILD


def website(request):
    return {
        "WEBSITE_NAME": "Kalsi Global Links",
        "VERSION": VERSION,
        "BUILD": BUILD,
    }