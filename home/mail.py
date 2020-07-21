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
            f'The Gin Shed enquiry:' {data['subject']},
            f'You have new message from {data['sender']}: \n{data['message']}'',
            ["carlyclark07@gmail.com"],
            fail_silently=False,
            )
    except SMTPAuthenticationError:
        messages.error(request, "There was a problem submitting your form")