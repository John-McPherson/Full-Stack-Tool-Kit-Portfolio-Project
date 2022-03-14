from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# STATUS = ((0,'Awaiting Approval'),(1, 'Approved'))
INGREDIENT_TYPES = ((0,'Base'),(1, 'Modifier'))

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
