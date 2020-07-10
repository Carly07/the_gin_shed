from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
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


def cocktail_recipe(request, recipe_id):
    """ A view to show the cocktail recipe """

    recipe = get_object_or_404(CocktailRecipe, pk=recipe_id)

    return render(request, 'cocktails/cocktail_recipe.html', {'recipe': recipe})


@login_required
def add_recipe(request):
    """ Add a cocktail recipe to the database """
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to add a recipe')
        return redirect(reverse('get_cocktails'))

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, {'user': request.user})
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe = form.save()
            messages.success(request, 'Your recipe has been saved!')
            return redirect(reverse('cocktail_recipe', args=[recipe.id]))
        else:
            messages.error(request, 'There was a problem saving your recipe. Please ensure the form is valid.')
    else:
        form = RecipeForm()

    template = 'cocktails/add_recipe.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_recipe(request, recipe_id):
    """ Edit a recipe in the database """
    recipe = get_object_or_404(CocktailRecipe, pk=recipe_id)

    if request.user == recipe.user or request.user.is_superuser:

        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES, instance=recipe)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated recipe!')
                return redirect(reverse('cocktail_recipe', args=[recipe.id]))
            else:
                messages.error(request, 'There was a problem updating the recipe. Please ensure the form is valid.')
        else:
            form = RecipeForm(instance=recipe)
            messages.info(request, f'You are editing {recipe.name}')

    else:
        messages.error(request, 'Sorry you do are not authorised to perform this action')
        return redirect(reverse('home'))

    template = 'cocktails/edit_recipe.html'
    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, template, context)


@login_required
def delete_recipe(request, recipe_id):
    """ Delete a recipe from the database """
    recipe = get_object_or_404(CocktailRecipe, pk=recipe_id)

    if request.user == recipe.user or request.user.is_superuser:
        recipe.delete()
        messages.success(request, 'Recipe Deleted!')
        return redirect('get_cocktails')
    messages.error(request, 'You are not authorised to delete this recipe.')
    return redirect('home')
