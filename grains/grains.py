def square(number):
    """
    This function calculates the number of wheat grain per square given that
    as the square number increases, the quantity of wheat per square doubles
    """
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    else:  
        if number > 1:
            grain_per_square = 1 << number - 1
        else:
            grain_per_square = 1

    return grain_per_square


def total():
    """
    This function calculates the number of wheat grain in a chess board
    """
    return ((1 << 64) - 1)
