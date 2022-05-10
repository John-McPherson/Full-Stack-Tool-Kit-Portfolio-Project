from random import randint
from .models import Recipe


def check_ingredients(user, update_type):
    """
    automatically updates the users recipes whenever they change their
    ingredients
    """

    user_ingredients = []

    if update_type == "base":
        user_ingredients.extend(user.user_ingredients)
        user_ingredients.extend(
            user.user_modifers.replace("[", "")
            .replace("'", "")
            .replace("]", "")
            .split(", ")
        )
    else:
        user_ingredients.extend(user.user_modifers)
        user_ingredients.extend(
            user.user_ingredients.replace("[", "")
            .replace("'", "")
            .replace("]", "")
            .split(", ")
        )

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
        drink_ingredients.extend(
            x[5]
            .replace("[", "")
            .replace("'", "")
            .replace("]", "")
            .split(", ")
        )
        drink_ingredients.extend(
            x[6]
            .replace("[", "")
            .replace("'", "")
            .replace("]", "")
            .split(", ")
        )
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
    if user.user_drinks:
        return Recipe.objects.filter(
            recipe_name=user.user_drinks[
                get_random_index(len(user.user_drinks))
            ]
        )
    else:
        return Recipe.objects.filter(recipe_name="No Recipes")


def get_random_index(index):
    """
    gets a random number to be used as an index to get a random drink recipe.

    """
    random = randint(0, index - 1)
    return random
