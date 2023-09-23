"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time:int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time =  EXPECTED_BAKE_TIME - elapsed_bake_time

    return remaining_bake_time



def preparation_time_in_minutes(layers:int):
    """
    :param layers : the number of layes added on the lasangna

    This function calculates and retun the number of minutes it will take to bake each lasagna
    based on the number of layers added
    """
    total_time = PREPARATION_TIME_PER_LAYER * layers
    
    return total_time



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """
    This function calculates the elapsed time the lasagna has been baking by first of all calculating
    the total preparation time (in minutes) and then adding it to the elapsed time.
    """

    total_preparation_time = number_of_layers * PREPARATION_TIME_PER_LAYER

    return elapsed_bake_time + total_preparation_time