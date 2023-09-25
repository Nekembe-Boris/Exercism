def square(number):
    """
    This function calculates the number of wheat grain per square given that
    as the square number increases, the quantity of wheat per square doubles
    """
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    else:
        grain_start = 1  
        if number > 1:
            for i in range(number-1):
                grain_start += grain_start
            grain_per_square = grain_start
        else:
            grain_per_square = 1

    return grain_per_square


def total():
    """
    This function calculates the number of wheat grain in a chess board
    """
    total =(2 ** 64) - 1

    return total
