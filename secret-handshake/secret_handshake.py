def commands(binary_str):
    sign = ['wink', 'double blink', 'close your eyes', 'jump']
    coded = []

    for index, num in enumerate(binary_str[1:][::-1]):
        if num == '1':
            coded.append(sign[index])

    if coded and binary_str[0] == '1':
        return coded[::-1]
    return coded
