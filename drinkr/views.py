from django.shortcuts import render
from django.views import generic, View
from .models import Ingredient, Recipe, UserData



def home_page(request):
    return render(request, '../templates/index.html')


class IngredientList(View):


    def get(self,request):
        model = Ingredient
        queryset = Ingredient.objects.filter(ingredient_type=0)
        ingredient_list = queryset
        user_ingredients = UserData.objects.filter(user_name=request.user).values_list('user_ingredients')
    

        return render(
            request,'update_ingredients.html',
            {
                 'ingredient_list' : queryset,
                 'user_ingredients' : list(user_ingredients)
            }
            )

    def post(self,request, *args, **kwargs):
        model = Ingredient
        queryset = Ingredient.objects.filter(ingredient_type=0)
        ingredient_list = queryset
        user_ingredients = UserData.objects.filter(user_name=request.user).values_list('user_ingredients')

        updated_user_ingredients = request.POST.getlist('ingredient')

        user = UserData.objects.get(user_name=request.user)
        user.user_ingredients = updated_user_ingredients
        user.save()


        return render(
            request,'update_ingredients.html',
            {
                 'ingredient_list' : queryset,
                 'user_ingredients' : list(user_ingredients),
            }
            )


class ModifierList(generic.ListView):
    model = Ingredient
    queryset = Ingredient.objects.filter(ingredient_type=1)
    template_name = 'update_modifiers.html'


class ConfirmRecipe(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(approved=1)
    template_name = 'confirm_recipe.html'

class DisplayRecipe(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(approved=1)
    template_name = 'recipe.html'
