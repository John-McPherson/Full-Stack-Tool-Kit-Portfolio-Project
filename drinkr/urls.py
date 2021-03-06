from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path(
        "update_ingredients",
        views.IngredientList.as_view(),
        name="ingredient_list",
    ),
    path(
        "update_modifiers",
        views.ModifierList.as_view(),
        name="modifier_list",
    ),
    path(
        "confirm_recipe",
        views.ConfirmRecipe.as_view(),
        name="confirm_recipe",
    ),
    path(
        "display_recipe",
        views.DisplayRecipe.as_view(),
        name="display_recipe",
    ),
    path(
        "submit_recipe",
        views.SubmitRecipe.as_view(),
        name="submit_recipe",
    ),
    path("user_favs", views.FavsList.as_view(), name="user_favs"),
    path(
        "account_details",
        views.AccountDetails.as_view(),
        name="account_details",
    ),
    path(
        "awaiting_approval",
        views.ApproveRecipes.as_view(),
        name="awaiting_approval",
    ),
]
