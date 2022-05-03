from django.shortcuts import render
from django.views import View
from .models import Ingredient, Recipe, UserData
from .recipe_checker import check_ingredients, get_random_recipe
from .new_recipe import (
    recipe_steps,
    ingredient_list,
    modifer_or_ingredient_list,
)
from .likes_dislikes import likes, likes_list, fav_drink_types
from .dob_check import dob_check

current_recipe = None


class home_page(View):
    def get(self, request):
        user_data_exists = False
        user_old_enough = False
        if request.user.is_authenticated:
            if UserData.objects.filter(user_name=request.user).exists():
                user_data_exists = True

                dob = UserData.objects.filter(user_name=request.user)
                user_old_enough = dob_check(dob[0].user_dob)

        return render(
            request,
            "index.html",
            {
                "UserDataExists": user_data_exists,
                "canUserDrink": user_old_enough,
            },
        )

    def post(self, request):
        data = UserData()
        data.user_name = request.user
        data.user_modifers = "[]"
        data.user_dob = request.POST.getlist("dob")[0]
        data.user_dislikes = "[]"
        data.user_favs = "[]"
        data.user_drinks = "[]"
        data.user_ingredients = "[]"
        user_old_enough = dob_check(data.user_dob)
        data.save()
        return render(
            request,
            "index.html",
            {"UserDataExists": True, "canUserDrink": user_old_enough},
        )


class IngredientList(View):
    def get(self, request):
        queryset = Ingredient.objects.filter(ingredient_type=0)
        user_ingredients = UserData.objects.filter(
            user_name=request.user
        ).values_list("user_ingredients")

        return render(
            request,
            "update_ingredients.html",
            {
                "ingredient_list": queryset,
                "user_ingredients": list(user_ingredients),
            },
        )

    def post(self, request, *args, **kwargs):
        queryset = Ingredient.objects.filter(ingredient_type=0)
        user_ingredients = UserData.objects.filter(
            user_name=request.user
        ).values_list("user_ingredients")

        updated_user_ingredients = request.POST.getlist("ingredient")

        user = UserData.objects.get(user_name=request.user)
        user.user_ingredients = updated_user_ingredients
        user.user_drinks = check_ingredients(user, "base")
        user.save()

        return render(
            request,
            "update_ingredients.html",
            {
                "ingredient_list": queryset,
                "user_ingredients": list(user_ingredients),
            },
        )


class ModifierList(View):
    def get(self, request):

        queryset = Ingredient.objects.filter(ingredient_type=1)

        user_ingredients = UserData.objects.filter(
            user_name=request.user
        ).values_list("user_modifers")

        return render(
            request,
            "update_modifiers.html",
            {
                "ingredient_list": queryset,
                "user_ingredients": list(user_ingredients),
            },
        )

    def post(self, request, *args, **kwargs):
        model = Ingredient
        queryset = Ingredient.objects.filter(ingredient_type=1)
        ingredient_list = queryset
        user_ingredients = UserData.objects.filter(
            user_name=request.user
        ).values_list("user_modifers")

        updated_user_ingredients = request.POST.getlist("ingredient")

        user = UserData.objects.get(user_name=request.user)
        user.user_modifers = updated_user_ingredients
        user.user_drinks = check_ingredients(user, "modifiers")
        user.save()
        global current_recipe
        current_recipe = get_random_recipe(user)

        return render(
            request, "confirm_recipe.html", {"recipe": current_recipe}
        )


class ConfirmRecipe(View):

    model = Recipe
    queryset = Recipe.objects.filter(approved=1)
    template_name = "confirm_recipe.html"


class DisplayRecipe(View):
    def get(self, request):
        steps = current_recipe[0].recipe_steps
        ingredients = current_recipe[0].ingredients_list

        return render(
            request,
            "recipe.html",
            {
                "recipe": current_recipe,
                "steps": likes_list(steps),
                "ingredients": likes_list(ingredients),
            },
        )

    def post(self, request, *args, **kwargs):

        user = UserData.objects.get(user_name=request.user)
        if request.POST.getlist("liked")[0] == "like":
            user.user_favs = likes(
                request.POST.getlist("drink_name")[0], user.user_favs
            )
            user.save()

        else:
            user.user_dislikes = likes(
                request.POST.getlist("drink_name")[0], user.user_dislikes
            )
            user.save()
        return render(request, "recipe.html", {"recipe": current_recipe})


class SubmitRecipe(View):
    def get(self, request):

        return render(
            request,
            "submit_recipe.html",
        )

    def post(self, request, *args, **kwargs):
        model = Recipe
        if Recipe.objects.filter(
            recipe_name=request.POST.get("drink-name").title()
        ).exists():
            title = request.POST.get("drink-name").title()
            does_recipe_exist = True
        else:
            recipe = Recipe()
            does_recipe_exist = False

            ingredients = request.POST.getlist("ingredient")
            measurement = request.POST.getlist("measurement")
            volume = request.POST.getlist("volume")
            title = request.POST.get("drink-name").title()

            recipe.recipe_name = title
            recipe.drink_type = 0
            recipe.approved = 0
            recipe.author = request.user
            recipe.ingredients = modifer_or_ingredient_list(
                request.POST.getlist("ingredient"), "ingredient"
            )
            recipe.modifiers = modifer_or_ingredient_list(
                request.POST.getlist("ingredient"), "modifier"
            )
            recipe.ingredients_list = ingredient_list(
                ingredients, measurement, volume
            )
            recipe.recipe_steps = recipe_steps(request.POST.getlist("step"))
            recipe.new_ingredients = modifer_or_ingredient_list(
                request.POST.getlist("ingredient"), "new"
            )
            recipe.save()

        return render(
            request,
            "form_submit.html",
            {"recipe_name": title, "exists": does_recipe_exist},
        )


class FavsList(View):
    def get(self, request, *args, **kwargs):

        favs = UserData.objects.get(user_name=request.user).user_favs

        return render(request, "favs.html", {"favs": fav_drink_types(favs)})

    def post(self, request, *args, **kwargs):
        drink_name = request.POST.get("drink_name")
        model = Recipe

        return render(
            request,
            "recipe.html",
            {"recipe": Recipe.objects.filter(recipe_name=drink_name)},
        )


class AccountDetails(View):
    def get(self, request, *args, **kwargs):
        # userData = UserData.objects.get(user_name=request.user)
        user = request.user
        return render(
            request,
            "account_details.html",
            {
                # 'user_data': userData,
                "user": user
            },
        )


class ApproveRecipes(View):
    def get(self, request, *args, **kwargs):
        model = Recipe
        queryset = Recipe.objects.filter(approved=0)
        if queryset[0].recipe_name == "No Recipes":
            try:
                recipe = queryset[1]
            except IndexError:
                recipe = queryset[0]
        else:
            recipe = queryset[0]
        new_ingredients = likes_list(recipe.new_ingredients)

        ingredients = likes_list(recipe.ingredients_list)
        steps = likes_list(recipe.recipe_steps)

        if new_ingredients[0] == "":
            new_ingredients = ["No New Ingredients"]
        else:
            # updates recipe with exisiting ingredients
            recipe_up = Recipe.objects.get(recipe_name=queryset[0].recipe_name)

            mods = likes_list(recipe_up.modifiers)
            ings = likes_list(recipe_up.ingredients)
            if ings[0] == "":
                recipe_up.ingredients = modifer_or_ingredient_list(
                    likes_list(recipe_up.new_ingredients), "ingredient"
                )
            else:
                recipe_up.ingredients = ings + modifer_or_ingredient_list(
                    likes_list(recipe_up.new_ingredients), "ingredient"
                )
            if mods[0] == "":
                recipe_up.modifiers = modifer_or_ingredient_list(
                    likes_list(recipe_up.new_ingredients), "modifier"
                )
            else:
                recipe_up.modifiers = mods + modifer_or_ingredient_list(
                    likes_list(recipe_up.new_ingredients), "modifier"
                )

        
            new_ingredients = modifer_or_ingredient_list(
                likes_list(recipe_up.new_ingredients), "new"
            )
            recipe_up.new_ingredients = new_ingredients
            recipe_up.save()
            if recipe_up.new_ingredients == "[]":
                new_ingredients = ["No New Ingredients"]

        return render(
            request,
            "awaiting_approval.html",
            {
                "recipe": recipe,
                "ingredients": ingredients,
                "new_ingredients": new_ingredients,
                "steps": steps,
            },
        )

    def post(self, request, *args, **kwargs):
        old_name = request.POST.get("old-name")
        drink = Recipe.objects.get(recipe_name=old_name)
        if request.POST.get("sub") == "reject":
            drink.delete()
        else:
            drink.recipe_name = request.POST.get("drink-name")
            recipe_steps = request.POST.getlist("step")
            drink.drink_type = request.POST.get("type")
            drink.approved = 1

            if drink.new_ingredients != "[]":
                drink.ingredients_list = request.POST.getlist("ingredient")
                mod = []
                base = []
                for x in likes_list(drink.new_ingredients):
                    ingredient = Ingredient()
                    if request.POST.getlist(x)[0] == "base":
                        base.append(x)
                        ingredient.ingredient_type = 0
                    elif request.POST.getlist(x)[0] == "modifier":
                        mod.append(x)
                        ingredient.ingredient_type = 1

                    ingredient.ingredient_name = x
                    ingredient.save()

                if likes_list(drink.ingredients)[0] == "":
                    drink.ingredients = base
                else:
                    drink.ingredients = likes_list(drink.ingredients) + base
                if likes_list(drink.modifiers)[0] == "":
                    drink.modifiers = mod
                else:
                    drink.modifiers = likes_list(drink.modifiers) + mod
                drink.new_ingredients = []
            drink.save()

        # model = Recipe
        # queryset = Recipe.objects.filter(approved=0)
        # ingredients = likes_list(queryset[0].ingredients_list)
        # recipe_steps = likes_list(queryset[0].recipe_steps)
        # new_ingredients = likes_list(queryset[0].new_ingredients)

        return render(
            request,
            "account_details.html",
            {
                # 'user_data': userData,
                "user": request.user
            },
        )
