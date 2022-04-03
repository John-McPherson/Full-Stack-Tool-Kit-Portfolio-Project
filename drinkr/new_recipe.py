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
    list = []
    y = 0 
    for ingredient in ingredients:
        if ingredient:
            line = f'{volume[y]} {measurement[y]} of {ingredient}'
            y+=1
            list.append(line)
    return list
