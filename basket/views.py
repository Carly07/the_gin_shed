from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """ A view to return the shopping basket contents """

    return render(request, 'basket/basket.html')
