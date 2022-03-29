from . import views
from .views import home_page 
from django.urls import path

urlpatterns = [
    path('', home_page, name='home'),
    path('update_ingredients', views.IngredientList.as_view(), name='ingredient_list'),
    path('update_modifiers', views.ModifierList.as_view(), name='modifier_list'),
    path('confirm_recipe', views.ConfirmRecipe.as_view(), name='confirm_recipe'),
    path('display_recipe', views.DisplayRecipe.as_view(), name='display_recipe'),
]