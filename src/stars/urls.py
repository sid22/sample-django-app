"""urls file of an application"""
from stars.views import home_page
from django.urls import path


urlpatterns = [
    path("", home_page, name="home_page"),
]
