from django.shortcuts import render
from django.views import generic, View
from .models import Ingredient, Recipe, UserData
from .recipe_checker import check_ingredients, get_random_recipe



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
        user.user_drinks = check_ingredients(user, 'base')
        user.save()


        return render(
            request,'update_ingredients.html',
            {
                 'ingredient_list' : queryset,
                 'user_ingredients' : list(user_ingredients),
            }
            )

class ModifierList(View):


    def get(self,request):
        model = Ingredient
        queryset = Ingredient.objects.filter(ingredient_type=1)
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
        queryset = Ingredient.objects.filter(ingredient_type=1)
        ingredient_list = queryset
        user_ingredients = UserData.objects.filter(user_name=request.user).values_list('user_modifers')

        updated_user_ingredients = request.POST.getlist('ingredient')

        user = UserData.objects.get(user_name=request.user)
        user.user_modifers = updated_user_ingredients
        user.user_drinks = check_ingredients(user, "modifiers")
        user.save()

        # get_random_recipe(user)


        return render(
            request,'recipe.html',
            {
                 'recipe' : get_random_recipe(user)
            }
            )



class ConfirmRecipe(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(approved=1)
    template_name = 'confirm_recipe.html'

class DisplayRecipe(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(approved=1)
    template_name = 'recipe.html'
