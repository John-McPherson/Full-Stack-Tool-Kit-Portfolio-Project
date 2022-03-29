from django.shortcuts import render
from django.views import generic, View
from .models import Ingredient


def home_page(request):
    return render(request, '../templates/index.html')


class IngredientList(generic.ListView):
    model = Ingredient
    queryset = Ingredient.objects.filter(ingredient_type=0)
    template_name = 'update_ingredients.html'


class ModifierList(generic.ListView):
    model = Ingredient
    queryset = Ingredient.objects.filter(ingredient_type=1)
    template_name = 'update_modifiers.html'