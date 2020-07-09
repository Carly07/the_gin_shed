from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from home.mail import send_contact_form

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def contact(request, *args, **kwargs):
    """
    A view to renders contact form on contact page with any
    relevant information the user has already provided in
    the name and email fields.
    """

    if request.user.is_authenticated:
        initial_data = {
            'name': request.user.first_name,
            'email': request.user.email
        }

        contact_form = ContactForm(initial=initial_data)

    else:
        contact_form = ContactForm()

    context = {
        "page": "contact",
        "form": contact_form,
    }

    if request.method == "POST":
        send_contact_mail(request)
        messages.success(request, "Thank You For Contatcting Us!")

    return render(request, 'home/contact.html', context)


def privacy(request):
    """ A view to return the privacy page """

    return render(request, 'home/privacy.html')


def terms(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/terms.html')
