plain =  "abcdefghijklmnopqrstuvwxyz"
cipher = plain[::-1]

def encode(plain_text:str):

    crypted = "".join([char if char.isdigit() else cipher[plain.index(char)] for char in plain_text.lower() if char.isalnum()])

    new_text = list(crypted)

    word_len = int(len(crypted) / 5)
    index = 5

    for _ in range(word_len):
        new_text.insert(index, " ")
        index += 6

    if new_text[-1] == " ":
        return "".join(new_text[:-1])
    return "".join(new_text)


def decode(ciphered_text:str):
    uncrypted = "".join([char if not char.isalpha() else plain[cipher.index(char)] for char in ciphered_text.lower()])

    return uncrypted.replace(" ", "")


# from string import ascii_lowercase
# ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

# def encode(text: str):
#     res = "".join(chr for chr in text.lower() if chr.isalnum()).translate(ENCODING)
#     return " ".join(res[index:index+5] for index in range(0, len(res), 5))

# def decode(text: str):
#     return "".join(chr.lower() for chr in text if chr.isalnum()).translate(ENCODING)