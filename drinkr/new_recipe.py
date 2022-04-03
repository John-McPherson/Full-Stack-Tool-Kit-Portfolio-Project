
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
    ing_list = []
    y = 0 
    for ingredient in ingredients:
        if ingredient:
            print(f'{volume[y]} {measurement[y]} of {ingredient.title()}')
            ing_list.append(f'{volume[y]} {measurement[y]} of {ingredient.title()}')
            y+=1
        else: 
            print("not working")
    print (ing_list)
    return ing_list

def modifer_or_ingredient_list(ingredients, type):
    """
    checks to see if an ingrdient is a modifier or an ingredient
    """
    ing_list = []
    new_ing_list = []
    for ingredient in ingredients:
        if ingredient:
            if type == "modifier":
                ing = Ingredient.objects.filter(ingredient_type=1).filter(ingredient_name=ingredient.title()).values_list()
                if ing:
                    ing_list.append(ingredient.title())    
            elif type =="ingredient": 
                ing = Ingredient.objects.filter(ingredient_type=0).filter(ingredient_name=ingredient.title()).values_list()
                # ing_list.append(ingredient.title())
                if ing:
                    ing_list.append(ingredient.title())
            else:
                ing = Ingredient.objects.filter(ingredient_name=ingredient.title()).values_list()
                if not ing:
                    new_ing_list.append(ingredient.title())
    if type == 'new':
        return new_ing_list
    else: 
        return ing_list
    # print(queryset)


