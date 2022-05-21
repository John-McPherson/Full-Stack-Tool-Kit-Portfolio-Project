from django.db import models
from django.contrib.auth.models import User

# Choices for integerFields in classes.
STATUS = ((0, "Awaiting Approval"), (1, "Approved"))
INGREDIENT_TYPES = ((0, "Base"), (1, "Modifier"))
DRINK_TYPES = ((0, "Up"), (1, "On The Rocks"), (2, "Long"))


class Ingredient(models.Model):
    """
    A class to represent cocktail ingredients
    ----------
    Attributes
    ----------
    ingredient_name: str
        The name of the ingredient
    ingredient_type: str
        The type of ingredient (if it is a modifier or a base ingredient)
    """

    ingredient_name = models.CharField(max_length=200, unique=True)
    ingredient_type = models.IntegerField(choices=INGREDIENT_TYPES, default=0)

    def __str__(self):
        return f"{self.ingredient_name}"


class Recipe(models.Model):
    """
    A class to represent cocktail recipes
    ----------
    Attributes
    ----------
    recipe_name: str
    drink_type: str
    recipe_steps: list
    ingredients_list: list
    ingredients: list
    modifiers: list
    new_ingredients: list
    author: str
    approved: boolean
    """

    recipe_name = models.CharField(max_length=200, unique=True)
    drink_type = models.IntegerField(choices=DRINK_TYPES, default=0)
    recipe_steps = models.TextField()
    ingredients_list = models.TextField()
    modifiers = models.TextField()
    ingredients = models.TextField()
    new_ingredients = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    approved = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.recipe_name}"


class UserData(models.Model):
    """
    A class to store user data away from senstive login infomation
    ----------
    Attributes
    ----------
    user_name: str
    user_dob: date
    user_ingredients: list
    user_modifers: list
    user_drinks: list
    user_favs: list
    user_dislikes: list
    """

    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_name"
    )
    user_dob = models.DateTimeField()
    user_ingredients = models.TextField(null=True)
    user_modifers = models.TextField(null=True)
    user_drinks = models.TextField(null=True)
    user_favs = models.TextField(null=True)
    user_dislikes = models.TextField(null=True)

    def __str__(self):
        return f"{self.user_name}"
