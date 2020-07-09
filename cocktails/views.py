from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from .models import CocktailRecipe
from .forms import RecipeForm


def get_cocktails(request):
    """
    Create a view that will return a list
    of Cocktail Recipes and render them to
    the 'cocktails.html' template
    """

    recipes = CocktailRecipe.objects.filter(published_date__lte=timezone.now()
            ).order_by('-published_date')
    return render(request, "cocktails/cocktails.html", {'recipes': recipes})
