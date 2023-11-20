def value(colors):
    color_li = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    values = [str(color_li.index(color)) for color in colors]
    return int("".join(values[:2]))
