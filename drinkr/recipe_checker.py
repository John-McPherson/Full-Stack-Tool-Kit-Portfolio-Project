from django.shortcuts import render
from django.views import generic, View
from .models import Ingredient, Recipe, UserData
from random import randint


def check_ingredients(user,update_type):
    """
    automatically updates the users recipes whenever they change their ingredients
    """
    
    # gets data from the database and prepares and converts it unto python lists

    user_ingredients = []

    if update_type == "base":
        user_ingredients.extend(user.user_ingredients)
        user_ingredients.extend(user.user_modifers.replace('[','').replace("'","").replace(']','').split(", "))
    else: 
        user_ingredients.extend(user.user_modifers)
        user_ingredients.extend(user.user_ingredients.replace('[','').replace("'","").replace(']','').split(", "))

    recipes = Recipe.objects.filter(approved=1).values_list()
    # creates an empty vairable to contain the data
    user_recipes = []

    # itterates through the recipes to see if the user has the ingredients. 
    for x in recipes:
        # creates an empty vairable to contain the users ingredients
        drink_ingredients = []
        # gets the recipe name
        drink_name = x[1]
        # adds the drinks modifers and base spirits into one list
        drink_ingredients.extend(x[5].replace('[','').replace("'","").replace(']','').split(", "))
        drink_ingredients.extend(x[6].replace('[','').replace("'","").replace(']','').split(", "))
        # checks to see if the ingredients exist in the users stock
        result = all(elm in user_ingredients for elm in drink_ingredients)
        if result:
            # adds the recipe name to the user_recipe list
            user_recipes.append(drink_name)
 
    # returns the final data to be used in the database
    return user_recipes

def get_random_recipe(user):
    """
    pulls a random recipe from the users drinks section
    """
    # get_random_index()
    recipe = Recipe.objects.filter(recipe_name=user.user_drinks[get_random_index(len(user.user_drinks))])
    # print(f'recipes {recipe} type {type(recipe)}')
    return recipe

def get_random_index(index):
    """
    gets a random number to be used as an index to get a random drink recipe.

    """
    random = randint(0,index-1)
    print(random)
    return(random)