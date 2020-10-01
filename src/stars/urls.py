"""urls file of an application"""
from stars.views import status, home_page
from django.urls import path


urlpatterns = [
    path("api/status/", status, name="status"),
    path("", home_page, name="home_page"),
]
