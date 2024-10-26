# weather/urls.py

from django.urls import path
from .views import weather_view  # Import your view

urlpatterns = [
    path('', weather_view, name='weather'),  # This will match the root URL
]
