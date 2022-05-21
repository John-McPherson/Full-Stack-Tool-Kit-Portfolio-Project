

def data_prep(str):
    """
    processes data and removes troublesome characters.
    """
    return str.replace(',','&#44;').replace("'", "&#39;").replace('"', "&#34;").replace("(", "&#40;").replace(")", '&#41;').replace(">", "&#62;").replace("<", "&#60;")
