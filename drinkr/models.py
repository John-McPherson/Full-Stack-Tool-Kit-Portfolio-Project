from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0,'Awaiting Approval'),(1, 'Approved'))
INGREDIENT_TYPES = ((0,'Base'),(1, 'Modifier'))
DRINK_TYPES = ((0,'Up'),(1, 'On The Rocks'), (2,'Long'))

class Ingredients(models.Model):
    '''
    A class to represent cocktail ingredients
    ....
    Attributes
    ----------
    ingredient_name: str
        The name of the ingredient
    ingredient_type: str 
        The type of ingredient (if it is a modifier or a base ingredient)
    '''
    ingredient_name = models.CharField(max=200,unique=True)
    ingredient_type = models.IntegerField(choices=INGREDIENT_TYPES, default=0)

    def __str__(self):
        return self.ingredient_name

class Recipes(models.Model):
    '''
    A class to represent cocktail recipes
     ....
    Attributes
    ----------
    recipe_name: str
    drink_type: str
    recipe_steps: list 
    ingredients_list: list
    modifiers: list
    author: str
    approved: boolean 
    '''
    recipe_name = models.CharField(max=200,unique=True)
    drink_type = models.IntegerField(choices=DRINK_TYPES, default=0)
    recipe_steps = models.TextField()
    ingredients_list = models.TextField()
    modifiers = models.TextField()
    ingredients = models.TextField()
    author = models.ForeignKey(USER, on_delete=models.CASCADE,related_name='recipie')
    approved =  models.IntegerField(choices=STATUS, default=0)

     def __str__(self):
        return self.recipe_name


