def return_val(char):

    if 0 <= int(char) < 1000:
        return f'{char} ohms'

    if 1000 <= int(char) < 1000000:
        if (val := int(char)/1000).is_integer():
            return f'{ int(val) } kiloohms'
        return f'{val} kiloohms'

    if 1000000 <= int(char) < 1000000000:
        if (val := int(char)/1000000).is_integer():
            return f'{ int(val) } megaohms'
        return f'{val} megaohms'


def resistor_label(colors):
    rgb = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

    tolerance = {'grey':0.05, 'violet':0.1, 'blue':0.25, 'green':0.5, 'brown':1, 'red':2, 'gold':5,  'silver':10}

    value = ''
    tol_val = 0

    if len(colors) > 1:
        for i, color in enumerate(colors[:-2]):
            if rgb.index(color) == 0 and i == 0:
                continue
            value += f"{rgb.index(color)}"

        value +=  '0' * rgb.index(colors[-2])

        resis_value = return_val(value)


        for key, val in tolerance.items():
            if key == colors[-1]:
                tol_val += val

        return f'{resis_value} ±{tol_val}%'

    return f'{rgb.index(colors[0])} ohms'
