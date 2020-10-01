from json import dumps
from urllib.parse import ParseResult, parse_qsl, unquote, urlencode, urlparse
from datetime import datetime
import requests
from django.conf import settings


def add_url_params(url, params):
    """Add GET params to provided URL being aware of existing.

    :param url: string of target URL
    :param params: dict containing requested params to be added
    :return: string with updated URL

    >> url = 'http://stackoverflow.com/test?answers=true'
    >> new_params = {'answers': False, 'data': ['some','values']}
    >> add_url_params(url, new_params)
    'http://stackoverflow.com/test?data=some&data=values&answers=false'
    """
    # Unquoting URL first so we don't loose existing args
    url = unquote(url)
    # Extracting url info
    parsed_url = urlparse(url)
    # Extracting URL arguments from parsed URL
    get_args = parsed_url.query
    # Converting URL arguments to dict
    parsed_get_args = dict(parse_qsl(get_args))
    # Merging URL arguments dict with new params
    parsed_get_args.update(params)

    # Bool and Dict values should be converted to json-friendly values
    # you may throw this part away if you don't like it :)
    parsed_get_args.update(
        {k: dumps(v) for k, v in parsed_get_args.items() if isinstance(v, (bool, dict))}
    )

    # Converting URL argument to proper query string
    encoded_get_args = urlencode(parsed_get_args, doseq=True)
    # Creating new parsed result object based on provided with new
    # URL arguments. Same thing happens inside of urlparse.
    new_url = ParseResult(
        parsed_url.scheme,
        parsed_url.netloc,
        parsed_url.path,
        parsed_url.params,
        encoded_get_args,
        parsed_url.fragment,
    ).geturl()

    return new_url


def _make_url(endpoint, api_key=True):
    url = settings.NASA_API_URL + endpoint
    if api_key:
        url = add_url_params(url=url, params={"api_key": settings.NASA_API_KEY})
    return url


def image_of_the_day():
    """
    Sample response
    response = {
        "copyright": "Damian Peach",
        "date": "2020-10-01",
        "explanation": "As telescopes around planet Earth watch, Mars is growing brighter in night skies, approaching its 2020 opposition on October 13. Mars looks like its watching too in this view of the Red Planet from September 22. Mars' disk is already near its maximum apparent size for earthbound telescopes, less than 1/80th the apparent diameter of a Full Moon. The seasonally shrinking south polar cap is at the bottom and hazy northern clouds are at the top. A circular, dark albedo feature, Solis Lacus (Lake of the Sun), is just below and left of disk center. Surrounded by a light area south of Valles Marineris, Solis Lacus looks like a planet-sized pupil, famously known as The Eye of Mars . Near the turn of the 20th century, astronomer and avid Mars watcher Percival Lowell associated the Eye of Mars with a conjunction of canals he charted in his drawings of the Red Planet. Broad, visible changes in the size and shape of the Eye of Mars are now understood from high resolution surface images to be due to dust transported by winds in the thin Martian atmosphere.",
        "hdurl": "https://apod.nasa.gov/apod/image/2010/m2020_09_22Adp.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Solis Lacus: The Eye of Mars",
        "url": "https://apod.nasa.gov/apod/image/2010/m2020_09_22Adp.jpg",
    }
    """
    url = _make_url(endpoint="planetary/apod")
    resp = requests.get(url)
    data = resp.json()
    return data


def epic():
    url = _make_url(endpoint="api/natural", api_key=False)
    resp = requests.get(url)
    # data = resp.json()
    data = [
        {
            "identifier": "20200929003634",
            "caption": "This image was taken by NASA's EPIC camera onboard the NOAA DSCOVR spacecraft",
            "image": "epic_1b_20200929003634",
            "version": "03",
            "centroid_coordinates": {
                "lat": -0.0073239999999999998,
                "lon": 174.42626999999999,
            },
            "dscovr_j2000_position": {
                "x": -1389254.9464459999,
                "y": -279895.53470999998,
                "z": 2866.11717,
            },
            "lunar_j2000_position": {
                "x": 358640.37965900003,
                "y": -144985.95600400001,
                "z": -98832.943742999996,
            },
            "sun_j2000_position": {
                "x": -149020886.83333099,
                "y": -14495394.000019001,
                "z": -6283650.0000080001,
            },
            "attitude_quaternions": {
                "q0": 0.546373,
                "q1": 0.055355000000000001,
                "q2": 0.082441,
                "q3": 0.83162999999999998,
            },
            "date": "2020-09-29 00:31:45",
            "coords": {
                "centroid_coordinates": {
                    "lat": -0.0073239999999999998,
                    "lon": 174.42626999999999,
                },
                "dscovr_j2000_position": {
                    "x": -1389254.9464459999,
                    "y": -279895.53470999998,
                    "z": 2866.11717,
                },
                "lunar_j2000_position": {
                    "x": 358640.37965900003,
                    "y": -144985.95600400001,
                    "z": -98832.943742999996,
                },
                "sun_j2000_position": {
                    "x": -149020886.83333099,
                    "y": -14495394.000019001,
                    "z": -6283650.0000080001,
                },
                "attitude_quaternions": {
                    "q0": 0.546373,
                    "q1": 0.055355000000000001,
                    "q2": 0.082441,
                    "q3": 0.83162999999999998,
                },
            },
        }
    ]
    img = data[0]
    img_date = datetime.strptime(img["date"], "%Y-%m-%d %X")
    img_url_endpoint = (
        "EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png".format(
            year=img_date.year,
            month=img_date.month,
            day=img_date.day,
            image=img["image"],
        )
    )
    img_url = _make_url(endpoint=img_url_endpoint)
    return img_url, img
