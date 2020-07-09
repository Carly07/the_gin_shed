from django.db import models
from django.utils import timezone


class CocktailRecipe(models.Model):
    """
    Model to define the fields required to create a Cocktail Recipe
    """
    name = models.CharField(max_length=200)
    serves = models.PositiveSmallIntegerField(blank=False, default=1)
    ingredients = models.TextField(blank=False)
    method = models.TextField(blank=False)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.name
