from .models import Recipe
from django import forms


class NewRecipeForm(forms.ModelForm):
    class Meta: 
        model = Recipe
        fields = ('recipe_name','recipe_steps','ingredients_list',)