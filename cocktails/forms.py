from django import forms
from .models import CocktailRecipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = CocktailRecipe
        fields = ('name', 'image', 'serves', 'ingredients', 'method', 'tag')
