def reverse(text):
    reversed_text = ""
    for index in range(-1, -(len(text)+1), -1):
        reversed_text += text[index]
    return reversed_text