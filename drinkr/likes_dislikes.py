from .models import Recipe

def likes(drink, likes):
    """
    checks to see if a drink exists in users likes
    """
    # likes_list = likes.replace('[','').replace("'","").replace('['',','').replace(']','').split(",")
    print(likes)
    print(type(likes))
    if drink[0] in likes:
        return likes
    else:
        if likes == "[]":
            likes = [drink]
        else:
            likes = likes.replace('[','').replace("'","").replace('['',','').replace(']','').split(",")
            likes.append(drink)
        return likes

def likes_list(data):
    """
    turns the data into a python list/ usable data
    """
    return data.replace('[','').replace("'","").replace("]","").replace("'',", "").split(',')


def fav_drink_types(favs):
    """
    gets an iterable list of drink types to display on the fav page
    """
    drinks = []
    loop_count = 0; 
    for fav in likes_list(favs):
        if loop_count != 0:
            fav = fav[1:]
        recipe = Recipe.objects.filter(recipe_name=fav)
        drink = [recipe[0].recipe_name,recipe[0].drink_type]
        print(drink)
        loop_count=+1
        drinks.append(drink) 
    return drinks
