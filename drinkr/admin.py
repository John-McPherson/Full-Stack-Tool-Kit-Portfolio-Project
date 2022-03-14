from django.contrib import admin
from .models import Ingredient, Recipe, UserData

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(UserData)
