vowels = ['a', 'e', 'i', 'o', 'u', 'xr', 'yt']


##UNFINISHED
def translate(text):
    for txt in text.split():
        if txt[0] in vowels or txt[:2] in vowels:
            return f'{txt}ay'
        if text[0] == 'y':
            return f'{txt[1:]}yay'
        if txt[:2] == 'qu':
            return f'{txt[2:]}quay'
        if txt[0] not in vowels:
            if txt[1:3] == 'qu':
                return f'{txt[3:]}{txt[:3]}ay'
            if txt[1] not in vowels:
                for i, letter in enumerate(txt):
                    if letter in vowels:
                        return f'{txt[i:]}{txt[:i]}ay'
            if 'y' in txt and txt.index('y') != 0:
                for i, letter in enumerate(txt):
                    if letter == 'y':
                        return f'{txt[i:]}{txt[:i]}ay'
            return f'{txt[1:]}{txt[0]}ay'
