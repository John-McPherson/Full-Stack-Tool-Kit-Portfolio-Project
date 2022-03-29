from . import views
from .views import home_page 
from django.urls import path

urlpatterns = [
    path('', home_page, name='home'),
    path('update_ingredients', views.IngredientList.as_view(), name='ingredient_list'),

]