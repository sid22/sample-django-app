from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

import stars.rnasa as nasa


def home_page(request):
    co_data = {
        "headquarters": {
            "address": "NASA",
            "city": "300 E St SW",
            "state": "Washington, DC",
        },
        "links": {
            "website": "https://nasa.gov/",
        },
        "name": "NASA",
        "summary": "The National Aeronautics and Space Administration is a U.S. Gov agency responsible for the civilian space program, as well as aeronautics and space research",
    }
    iotd = nasa.image_of_the_day()
    return render(
        request,
        "home_page.html",
        {"company_info": co_data, "iotd": iotd, "nasa_api_key": settings.NASA_API_KEY},
    )
