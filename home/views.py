from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


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

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get['name']
            email = form.cleaned_data.get['email']
            message = form.cleaned_data.get['message']

            try:
                send_mail(name, message, email, ['carlyclark07@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            messages.success(request, "Thank you for your message. We'll be in touch shortly.")
            return redirect('home')
    return render(request, "home/contact.html", {'form': form})


def privacy(request):
    """ A view to return the privacy page """

    return render(request, 'home/privacy.html')


def terms(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/terms.html')
