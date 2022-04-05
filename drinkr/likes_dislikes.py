

def likes(drink, likes):
    """
    checks to see if a drink exists in users likes
    """
    likes = likes.replace('[','').replace("'","").replace(']','').split(", ")
    if drink[0] in likes:
        return likes
    else:
        likes.append(drink)
        return likes
