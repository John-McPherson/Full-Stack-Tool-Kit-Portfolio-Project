from django.contrib import admin
from .models import Ingredients, Recipes, UserData

# Register your models here.

admin.site.register(Ingredients)
admin.site.register(Recipes)
admin.site.register(UserData)
