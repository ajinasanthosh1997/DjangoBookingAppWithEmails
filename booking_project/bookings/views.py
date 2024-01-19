# bookings/views.py

from django.shortcuts import render, redirect
from .forms import BookingForm
import requests
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def index(request):
    return render(request,'bookings/index.html')

def contact(request):
    # You can add any necessary logic here
    return render(request, 'bookings/contact.html')

def about(request):
    # You can add any necessary logic here
    return render(request, 'bookings/about.html')    

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # Send confirmation email
            send_booking_confirmation_email(booking)

            return redirect('bookings:booking_success')  # Replace 'success_url' with your desired success URL
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})

def send_booking_confirmation_email(booking):
    subject = 'Booking Confirmation'

    # Render the HTML template
    html_message = render_to_string('bookings/booking_confirmation_email.html', {'booking': booking})

    # Create plain text version from HTML for clients that don't support HTML emails
    plain_message = strip_tags(html_message)

    # Create the email message with both plain text and HTML content
    email = EmailMultiAlternatives(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [booking.email],
    )
    email.attach_alternative(html_message, "text/html")

    try:
        # Send the email
        email.send(fail_silently=False)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def booking_success(request):
    return render(request, 'bookings/booking_success.html')
