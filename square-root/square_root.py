def square_root(number):
    for i in range(1, number):
        if i**2 == number:
            return i
    return 1