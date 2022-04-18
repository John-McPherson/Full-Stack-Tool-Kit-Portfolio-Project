from django.shortcuts import render
from django.views import generic, View
from .models import Ingredient, Recipe, UserData
from .recipe_checker import check_ingredients, get_random_recipe
from .new_recipe import recipe_steps, ingredient_list, modifer_or_ingredient_list
from . likes_dislikes import likes, likes_list, fav_drink_types
import numpy as np
current_recipe = None

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
        user_ingredients = UserData.objects.filter(user_name=request.user).values_list('user_modifers')
    

        return render(
            request,'update_modifiers.html',
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
        global current_recipe 
        current_recipe = get_random_recipe(user)



        return render(
            request,'confirm_recipe.html',
            {
                 'recipe' : current_recipe
            }
            )



class ConfirmRecipe(View):
    
    model = Recipe
    queryset = Recipe.objects.filter(approved=1)
    template_name = 'confirm_recipe.html'

class DisplayRecipe(View):

    def get(self,request):
    

        return render(
            request,'recipe.html',
            {
                 'recipe' : current_recipe
            }
            )
    
    def post(self,request, *args, **kwargs):

        user = UserData.objects.get(user_name=request.user)
        if request.POST.getlist('liked')[0] == 'like': 
            user.user_favs = likes(request.POST.getlist('drink_name')[0], user.user_favs)
            user.save()

        else: 
            user.user_dislikes = likes(request.POST.getlist('drink_name')[0], user.user_dislikes)
            user.save()
        return render(
            request,'recipe.html',
            {
                 'recipe' : current_recipe
            }
            )
    


class SubmitRecipe(View):


    def get(self,request):

        return render(
            request,'submit_recipe.html',
           
            )

    def post(self,request, *args, **kwargs):
        model = Recipe
        if Recipe.objects.filter(recipe_name=request.POST.get('drink-name').title()).exists():
            title = request.POST.get('drink-name').title()
            does_recipe_exist = True
        else:
            recipe = Recipe()
            does_recipe_exist = False

            ingredients = modifer_or_ingredient_list(request.POST.getlist('ingredient'), 'ingredient')
            measurement = request.POST.getlist('measurement')
            volume = request.POST.getlist('volume')
            title = request.POST.get('drink-name').title()

            recipe.recipe_name = title
            recipe.drink_type = 0
            recipe.approved = 0
            recipe.author = request.user
            recipe.ingredients = modifer_or_ingredient_list(request.POST.getlist('ingredient'), 'ingredient')
            recipe.modifiers = modifer_or_ingredient_list(request.POST.getlist('ingredient'), 'modifier')
            recipe.ingredients_list = ingredient_list(ingredients, measurement, volume)
            recipe.recipe_steps = recipe_steps(request.POST.getlist('step'))
            recipe.new_ingredients = modifer_or_ingredient_list(request.POST.getlist('ingredient'), 'new')
            recipe.save()


        return render(
            request,'form_submit.html',{
                'recipe_name': title , 
                'exists': does_recipe_exist
            }  
            )


class FavsList(View):

    def get(self,request, *args, **kwargs):

        favs = UserData.objects.get(user_name=request.user).user_favs
        
        return render(
            request, 'favs.html', {
            'favs': fav_drink_types(favs)
        })

    def post(self,request, *args, **kwargs):
        drink_name = request.POST.get('drink_name')
        model = Recipe


        return render(
            request,'recipe.html',
            {
                 'recipe' : Recipe.objects.filter(recipe_name=drink_name)
            })

class AccountDetails(View):
    def get(self,request, *args, **kwargs):
        # userData = UserData.objects.get(user_name=request.user)
        user = request.user
        return render(
            request,'account_details.html', {
            # 'user_data': userData,
            'user': user
        })


class ApproveRecipes(View):
    def get(self,request, *args, **kwargs):
        model = Recipe
        queryset = Recipe.objects.filter(approved=0)
        if queryset[0].recipe_name == "No Recipes":
            try:
                recipe = queryset[1]
            except IndexError:
                recipe = queryset[0]
        else: 
            recipe = queryset[0]
        ingredients = likes_list(recipe.ingredients_list)
        steps = likes_list(recipe.recipe_steps)
        new_ingredients = likes_list(recipe.new_ingredients)
       

        return render(
            request,'awaiting_approval.html', {
            'recipe': recipe,
            'ingredients': ingredients,
            'new_ingredients': new_ingredients,
            'steps': steps
        })

    def post(self,request, *args, **kwargs):
        old_name = request.POST.get('old-name')
        drink = Recipe.objects.get(recipe_name=old_name)

        drink.recipe_name = request.POST.get('drink-name')
        recipe_steps = request.POST.getlist('step')
        drink.ingredients_list = request.POST.getlist('ingredient')
        drink.approved = 1
        mod = []
        base = []
        for x in likes_list(drink.new_ingredients):

            ingredient = Ingredient()
            if request.POST.getlist(x)[0] == "base":
                base.append(x)
                ingredient.ingredient_type = 0
            else:
                mod.append(x)
                ingredient.ingredient_type = 1
            ingredient.ingredient_name = x 
            ingredient.save()
        drink.ingredients = likes_list(drink.ingredients) + base
        drink.modifiers = likes_list(drink.modifiers) + mod
        drink.new_ingredients = []
        drink.save()


        model = Recipe
        queryset = Recipe.objects.filter(approved=0)
        ingredients = likes_list(queryset[0].ingredients_list)
        recipe_steps = likes_list(queryset[0].recipe_steps)
        new_ingredients = likes_list(queryset[0].new_ingredients)

        return render(
            request,'awaiting_approval.html', {
            'recipe': queryset[0],
            'ingredients': ingredients,
            'new_ingredients': new_ingredients,
            'steps': recipe_steps
        })
