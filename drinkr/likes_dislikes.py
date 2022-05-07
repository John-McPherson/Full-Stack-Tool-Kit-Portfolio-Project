from .models import Recipe


def likes(drink, likes):
    """
    checks to see if a drink exists in users likes
    """
    print(likes)

    if drink[0] in likes:
        return likes
    else:
        if likes == "['No Recipes']":
            likes = [drink]
        else:
            likes = likes_list(likes)
            print(likes)
            print(type(likes))
            likes.append(drink)
        return likes


def likes_list(data):
    """
    turns the data into a python list/ usable data
    """
    new_list = []
    data = (
        data.replace("[", "")
        .replace("'", "")
        .replace("]", "")
        .replace("'',", "")
        .split(",")
    )
    loop_count = 0
    for item in data:
        if loop_count != 0:
            item = item[1:]
        loop_count = +1
        new_list.append(item)
    return new_list


def fav_drink_types(favs):
    """
    gets an iterable list of drink types to display on the fav page
    """
    drinks = []
    loop_count = 0

    for fav in likes_list(favs):
        print(f"loop {loop_count}")
        recipe = Recipe.objects.filter(recipe_name=fav)
        drink = [recipe[0].recipe_name, recipe[0].drink_type]
        loop_count = +1
        drinks.append(drink)
    return drinks
