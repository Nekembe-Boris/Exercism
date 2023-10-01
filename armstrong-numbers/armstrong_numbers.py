"""module checks if an int is an Armstong number"""
def is_armstrong_number(number:int):
    """
    :param number - integer to be verified

    Determines whether a number is an Armstrong number
    """
    total = 0

    for i in str(number):
        total += int(i) ** len(str(number))

    return total == number


is_armstrong_number(9)
