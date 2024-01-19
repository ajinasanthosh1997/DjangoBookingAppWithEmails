# bookings/urls.py

from django.urls import path
from .views import create_booking,booking_success,index,contact,about

app_name='bookings'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('booking/', create_booking, name='create_booking'),
    path('success/', booking_success, name='booking_success'),
]
