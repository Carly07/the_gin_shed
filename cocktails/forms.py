from django import forms
from .widgets import CustomClearableFileInput
from .models import CocktailRecipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = CocktailRecipe
        fields = ('name', 'serves', 'ingredients', 'method', 'tag', 'image')

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
            self.fields['ingredients'].widget.attrs['rows'] = 5
            self.fields['method'].widget.attrs['rows'] = 5
