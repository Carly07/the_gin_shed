from django.contrib import admin
from .models import CocktailRecipe

# Register your models here.


class CocktailAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'published_date',
        'image',
        'user',
    )

    ordering = ('published_date',)


admin.site.register(CocktailRecipe, CocktailAdmin)
