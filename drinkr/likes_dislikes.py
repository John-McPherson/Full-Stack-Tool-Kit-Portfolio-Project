

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