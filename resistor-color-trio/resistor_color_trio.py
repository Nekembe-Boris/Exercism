def label(colors):
    rgb = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    value = ''

    for i, color in enumerate(colors[:2]):
        if i == 0 and rgb.index(color) == 0:
            continue
        value += f"{rgb.index(color)}"

    value = value + ("0" * rgb.index(colors[2]))

    if value.count("0") >= 9:
        return f"{value[:-9]} gigaohms"

    if value.count("0") >= 6:
        return f"{value[:-6]} megaohms"

    if value.count("0") >= 3:
        return f"{value[:-3]} kiloohms"

    return f"{value} ohms"

