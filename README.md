# Django Booking Project

This is a Django-based web application for handling bookings. Users can create bookings through a web interface, and the system sends confirmation emails.

## Features

- User-friendly booking creation form.
- Email confirmation for successful bookings.
- Responsive design for various devices.

## Getting Started

### Prerequisites

- Python (3.6 or higher)
- Django (3.2 or higher)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/django-booking-project.git
   
2. Navigate to the project directory:

cd django-booking-project

3. Install dependencies:

pip install -r requirements.txt

5. Create and apply database migrations:

python manage.py makemigrations
python manage.py migrate

6. Create a .env file in the project root with the necessary settings:

DEBUG=True

SECRET_KEY=your_secret_key

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend

EMAIL_HOST=your_email_host

EMAIL_PORT=your_email_port

EMAIL_USE_TLS=True

EMAIL_HOST_USER=your_email@example.com

EMAIL_HOST_PASSWORD=your_email_password

DEFAULT_FROM_EMAIL=your_email@example.com

7. Run the development server:

python manage.py runserver

Access the application at http://127.0.0.1:8000/

8. Usage
   
Open your web browser and go to http://127.0.0.1:8000/
Visit the booking form page.
Fill in the required details and submit the form.
You will be redirected to the booking success page.
Check your email for the booking confirmation.
