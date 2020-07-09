from smtplib import SMTPAuthenticationError

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


def send_contact_form(request):
    """
    send contact form as email
    """
    data = request.POST
    try:
        send_mail(
            f'The Gin Shed enquiry',
            f"You have new message from {data['name']} {data['email']}: \n{data['message']}",
            settings.FROM_EMAIL,
            ["carlyclark07@gmail.com"],
            fail_silently=False,
        )
    except SMTPAuthenticationError:
        messages.error(request, "There was a problem submitting your form")