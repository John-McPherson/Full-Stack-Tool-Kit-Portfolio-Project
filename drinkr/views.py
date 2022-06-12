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


class HomePage(View):
    """
    loads the home page
    """

    def get(self, request):
        """
        checks to see that the user exists and is old enough to drink.
        """
        user_data_exists = False
        user_old_enough = False
        index = "login_landing_page.html"
        if request.user.is_authenticated:
            index = "landing_page.html"
            if UserData.objects.filter(user_name=request.user).exists():
                user_data_exists = True

                dob = UserData.objects.filter(user_name=request.user)
                user_old_enough = dob_check(dob[0].user_dob)
                if user_old_enough:
                    index = "base.html"

        return render(
            request,
            "index.html",
            {
                "UserDataExists": user_data_exists,
                "canUserDrink": user_old_enough,
                "index": index,
            },
        )

    def post(self, request):
        """
        if the user is logging on for the first time
        a form will be loaded to complete the rest of
        the userData.
        """
        data = UserData()
        data.user_name = request.user
        data.user_modifers = "[]"
        data.user_dob = request.POST.getlist("dob")[0]
        data.user_dislikes = "['No Recipes']"
        data.user_favs = "['No Recipes']"
        data.user_drinks = "['No Recipes']"
        data.user_ingredients = "[]"
        user_old_enough = dob_check(data.user_dob)
        data.save()
        index = "landing_page.html"
        if user_old_enough:
            index = "base.html"

        return render(
            request,
            "index.html",
            {"UserDataExists": True, "canUserDrink": user_old_enough, "index": index},
        )


class IngredientList(View):
    """
    loads the update ingredient page
    """

    def get(self, request):
        """
        gets the full list of ingredients and a full list of
        the ingredients the user has so that the form to update
        can be prefillled out as much as possible.
        """
        queryset = Ingredient.objects.filter(ingredient_type=0)
        user_ingredients = UserData.objects.filter(user_name=request.user).values_list(
            "user_ingredients"
        )

        return render(
            request,
            "update_ingredients.html",
            {
                "ingredient_list": queryset,
                "user_ingredients": list(user_ingredients),
                "btn_text": "UPDATE",
            },
        )

    def post(self, request):
        """
        updates the user's ingredient list with the form data.
        """
        updated_user_ingredients = request.POST.getlist("ingredient")
        user = UserData.objects.get(user_name=request.user)
        user.user_ingredients = updated_user_ingredients
        user.user_drinks = check_ingredients(user, "base")
        user.save()

        return render(
            request,
            "update_ingredients.html",
            {
                "ingredient_list": Ingredient.objects.filter(ingredient_type=0),
                "user_ingredients": list(
                    UserData.objects.filter(user_name=request.user).values_list(
                        "user_ingredients"
                    )
                ),
                "btn_text": "UPDATED",
            },
        )


class ModifierList(View):
    """
    loads the update user modifer page
    """

    def get(self, request):
        """
        gets the full list of modifiers to create a form and
        prepopulates it with the user's list of modifiers
        """
        queryset = Ingredient.objects.filter(ingredient_type=1)
        user_ingredients = UserData.objects.filter(user_name=request.user).values_list(
            "user_modifers"
        )

        return render(
            request,
            "update_modifiers.html",
            {
                "ingredient_list": queryset,
                "user_ingredients": list(user_ingredients),
            },
        )

    def post(self, request):
        """
        Updates the user's modifiers with form data and
        updates the user recipe list.
        """
        updated_user_ingredients = request.POST.getlist("ingredient")
        user = UserData.objects.get(user_name=request.user)
        user.user_modifers = updated_user_ingredients
        # uses the updated user_ingredients to work out what
        # drinks the user can make
        user.user_drinks = check_ingredients(user, "modifiers")
        user.save()
        # sets the global current recipe so that it can be
        # accessed by other views
        global current_recipe
        current_recipe = get_random_recipe(user)
        return render(request, "confirm_recipe.html", {"recipe": current_recipe})


class ConfirmRecipe(View):
    """
    lets the user confirm that they want to make the drink
     generated for them
    """

    model = Recipe
    queryset = Recipe.objects.filter(approved=1)
    template_name = "confirm_recipe.html"


class DisplayRecipe(View):
    """
    loads the selected recipe and generates a list of steps
    and ingredients
    """

    def get(self, request):
        """
        loads the selected recipe
        """
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

    def post(self, request):
        """
        if the user likes/dislikes a drink it adds it to the
        users liked/ disliked drinks
        """
        steps = current_recipe[0].recipe_steps
        ingredients = current_recipe[0].ingredients_list

        user = UserData.objects.get(user_name=request.user)
        if request.POST.getlist("liked")[0] == "like":
            user.user_favs = likes(
                request.POST.getlist("drink_name")[0], user.user_favs
            )
            print(request.POST.getlist("drink_name")[0])
            user.save()

        else:
            user.user_dislikes = likes(
                request.POST.getlist("drink_name")[0],
                user.user_dislikes,
            )
            user.save()
        return render(
            request,
            "recipe.html",
            {
                "recipe": current_recipe,
                "steps": likes_list(steps),
                "ingredients": likes_list(ingredients),
            },
        )


class SubmitRecipe(View):
    """
    allows the user to submit recipes
    """

    def get(self, request):
        """
        loads the submit recipe form
        """
        return render(
            request,
            "submit_recipe.html",
        )

    def post(self, request):
        """
        checks to see if the recipe name already exists
        and if not adds it recipe list
        """
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
            recipe.ingredients_list = ingredient_list(ingredients, measurement, volume)
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
    """
    loads the users liked drinks
    """

    def get(self, request):
        """
        loads fav list page and loads it with users liked
        drinks
        """
        favs = UserData.objects.get(user_name=request.user).user_favs
        if len(likes_list(favs)) == 1:
            no_favs = True
        else:
            no_favs = False

        return render(
            request,
            "favs.html",
            {"favs": fav_drink_types(favs), "no_favs": no_favs},
        )

    def post(self, request):
        """
        loads the recipe page for the drink the user selects
        """
        drink_name = request.POST.get("drink_name")
        recipe = Recipe.objects.filter(recipe_name=request.POST.get("drink_name"))
        return render(
            request,
            "recipe.html",
            {
                "recipe": Recipe.objects.filter(recipe_name=drink_name),
                "steps": likes_list(recipe[0].recipe_steps),
                "ingredients": likes_list(recipe[0].ingredients_list),
            },
        )


class AccountDetails(View):
    """
    opens the users account management page
    """

    def get(self, request):
        """
        gets the user's data and loads their details
        """
        user_data = UserData.objects.get(user_name=request.user)

        return render(
            request,
            "account_details.html",
            {
                "user_data": user_data,
                "user": request.user,
            },
        )

    def post(self, request):
        """
        updates user DOB
        """
        user_data = UserData.objects.get(user_name=request.user)
        user_data.user_dob = request.POST.getlist("dob")[0]
        user_data.save()
        return render(
            request,
            "account_details.html",
            {
                "user_data": user_data,
                "user": request.user,
            },
        )


class ApproveRecipes(View):
    """
    allows superuser to approve recipes from the application
    """

    def get(self, request):
        """
        loads a recipe that hasn't been approved. Checks if
        ingredients are modifers or ingredients and sorts them into
        the correct place.
        """

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
                    likes_list(recipe_up.new_ingredients),
                    "ingredient",
                )
            else:
                recipe_up.ingredients = ings + modifer_or_ingredient_list(
                    likes_list(recipe_up.new_ingredients),
                    "ingredient",
                )
            if mods[0] == "":
                recipe_up.modifiers = modifer_or_ingredient_list(
                    likes_list(recipe_up.new_ingredients), "modifier"
                )
            else:
                recipe_up.modifiers = mods + modifer_or_ingredient_list(
                    likes_list(recipe_up.new_ingredients),
                    "modifier",
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

    def post(self, request):
        """
        takes the form data and updates the recipe
        or deletes it if applicable
        """
        old_name = request.POST.get("old-name")
        drink = Recipe.objects.get(recipe_name=old_name)
        if request.POST.get("sub") == "reject":
            drink.delete()
        else:
            drink.recipe_name = request.POST.get("drink-name")
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
        user_data = UserData.objects.get(user_name=request.user)

        return render(
            request,
            "account_details.html",
            {"user_data": user_data, "user": request.user},
        )
