"""urls file of an application"""
from stars.views import status
from django.urls import path


urlpatterns = [
    path("api/status/", status, name="status"),
]
