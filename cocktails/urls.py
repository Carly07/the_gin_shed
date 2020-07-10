from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_cocktails, name='get_cocktails'),
    path('<int:recipe_id>/', views.cocktail_recipe, name='cocktail_recipe'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('edit-recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]
