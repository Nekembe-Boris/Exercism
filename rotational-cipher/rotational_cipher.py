alphabets = "abcdefghijklmnopqrstuvwxyz"


def rotate(text:str, key):
    coded = ""

    for letter in text:
        if letter.isalpha():
            try:
                new_index = alphabets.index(letter) + key
            except ValueError:
                new_index = alphabets.index(letter.lower()) + key
            if new_index >= 26:
                new_index = new_index - 26

            if letter.islower():
                coded += alphabets[new_index]
            else:
                coded += alphabets[new_index].upper()
        else:
            coded += letter

    return coded
