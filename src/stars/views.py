from django.http import HttpResponse
from django.shortcuts import render

import stars.rnasa as nasa


# Create your views here.
def status(request):
    return HttpResponse("working")


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
    # iotd = nasa.image_of_the_day()
    iotd = {
        "copyright": "Damian Peach",
        "date": "2020-10-01",
        "explanation": "As telescopes around planet Earth watch, Mars is growing brighter in night skies, approaching its 2020 opposition on October 13. Mars looks like its watching too in this view of the Red Planet from September 22. Mars' disk is already near its maximum apparent size for earthbound telescopes, less than 1/80th the apparent diameter of a Full Moon. The seasonally shrinking south polar cap is at the bottom and hazy northern clouds are at the top. A circular, dark albedo feature, Solis Lacus (Lake of the Sun), is just below and left of disk center. Surrounded by a light area south of Valles Marineris, Solis Lacus looks like a planet-sized pupil, famously known as The Eye of Mars . Near the turn of the 20th century, astronomer and avid Mars watcher Percival Lowell associated the Eye of Mars with a conjunction of canals he charted in his drawings of the Red Planet. Broad, visible changes in the size and shape of the Eye of Mars are now understood from high resolution surface images to be due to dust transported by winds in the thin Martian atmosphere.",
        "hdurl": "https://apod.nasa.gov/apod/image/2010/m2020_09_22Adp.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Solis Lacus: The Eye of Mars",
        "url": "https://apod.nasa.gov/apod/image/2010/m2020_09_22Adp.jpg",
    }
    # epic_url, epic_data = nasa.epic()
    # epic_url = "https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key=DEMO_KEY"
    # epic_data = {
    #     "identifier": "20200929003634",
    #     "caption": "This image was taken by NASA's EPIC camera onboard the NOAA DSCOVR spacecraft",
    #     "image": "epic_1b_20200929003634",
    #     "version": "03",
    #     "centroid_coordinates": {
    #         "lat": -0.0073239999999999998,
    #         "lon": 174.42626999999999
    #     },
    #     "dscovr_j2000_position": {
    #         "x": -1389254.9464459999,
    #         "y": -279895.53470999998,
    #         "z": 2866.11717
    #     },
    #     "lunar_j2000_position": {
    #         "x": 358640.37965900003,
    #         "y": -144985.95600400001,
    #         "z": -98832.943742999996
    #     },
    #     "sun_j2000_position": {
    #         "x": -149020886.83333099,
    #         "y": -14495394.000019001,
    #         "z": -6283650.0000080001
    #     },
    #     "attitude_quaternions": {
    #         "q0": 0.546373,
    #         "q1": 0.055355000000000001,
    #         "q2": 0.082441,
    #         "q3": 0.83162999999999998
    #     },
    #     "date": "2020-09-29 00:31:45",
    #     "coords": {
    #         "centroid_coordinates": {
    #             "lat": -0.0073239999999999998,
    #             "lon": 174.42626999999999
    #         },
    #         "dscovr_j2000_position": {
    #             "x": -1389254.9464459999,
    #             "y": -279895.53470999998,
    #             "z": 2866.11717
    #         },
    #         "lunar_j2000_position": {
    #             "x": 358640.37965900003,
    #             "y": -144985.95600400001,
    #             "z": -98832.943742999996
    #         },
    #         "sun_j2000_position": {
    #             "x": -149020886.83333099,
    #             "y": -14495394.000019001,
    #             "z": -6283650.0000080001
    #         },
    #         "attitude_quaternions": {
    #             "q0": 0.546373,
    #             "q1": 0.055355000000000001,
    #             "q2": 0.082441,
    #             "q3": 0.83162999999999998
    #         }
    #     }
    # }
    return render(
        request,
        "home_page.html",
        {"company_info": co_data, "iotd": iotd, "insight": ""},
    )
