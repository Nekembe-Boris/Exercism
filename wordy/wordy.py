def is_num(char):
    try:
        int(char)
        return True
    except ValueError:
        return False

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def answer(question):
    num_list = []
    op_list = []

    operations = {
        'plus' : add,
        'minus' : subtract,
        'multiplied' : multiply,
        'divided' : divide
    }

    split_list = question[:-1].split(" ")
