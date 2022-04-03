
from .models import Ingredient, Recipe, UserData

def recipe_steps(recipe):
    """
    Gets the steps from from and formats them into usable data
    """
    steps = []
    x = 1
    for step in recipe:
        if step: 
            steps.append(f'{x}. {step.capitalize()}')
            x+=1
    return steps

def ingredient_list(ingredients,measurement, volume):
    """
    Converts form data ingredient, measurement, and volume into usable data
    """
    step_list = []
    y = 0 
    for ingredient in ingredients:
        if ingredient:
            line = f'{volume[y]} {measurement[y]} of {ingredient.title()}'
            y+=1
            step_list.append(line)
    return step_list

def modifer_or_ingredient_list(ingredients, type):
    """
    checks to see if an ingrdient is a modifier or an ingredient
    """
    ing_list = []
    new_ing_list = []
    for ingredient in ingredients:
        if ingredient:
            if type == "modifier":
                ing = Ingredient.objects.filter(ingredient_type=1).filter(ingredient_name=ingredient).values_list()
            else: 
                ing = Ingredient.objects.filter(ingredient_type=0).filter(ingredient_name=ingredient).values_list()
            if ing:
                ing_list.append(ingredient)
            else:
                new_ing_list.append(ingredient)
    if type == 'new':
        return new_ing_list
    else: 
        return ing_list
    # print(queryset)


