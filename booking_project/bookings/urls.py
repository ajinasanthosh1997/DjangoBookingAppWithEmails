# bookings/urls.py

from django.urls import path
from .views import create_booking,booking_success

app_name='bookings'

urlpatterns = [
    path('', create_booking, name='create_booking'),
    path('success/', booking_success, name='booking_success'),
]
