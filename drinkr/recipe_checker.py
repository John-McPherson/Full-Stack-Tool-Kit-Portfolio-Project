from django.shortcuts import render
from django.views import generic, View
from .models import Ingredient, Recipe, UserData


def check_ingredients(user):

    recipes = Recipe.objects.filter(approved=1).values_list()
    user_ingredients = user.user_ingredients
    user_ingredients.extend(user.user_modifers.replace('[','').replace("'","").replace(']','').split(", "))
    user_recipes = []

    for x in recipes:
        drink_ingredients = []
        drink_name = x[1]
        drink_ingredients.extend(x[5].replace('[','').replace("'","").replace(']','').split(", "))
        drink_ingredients.extend(x[6].replace('[','').replace("'","").replace(']','').split(", "))
        result = all(elm in user_ingredients for elm in drink_ingredients)
        if result:
            user_recipes.append(drink_name)
 
    
    return user_recipes

