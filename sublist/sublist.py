"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(one, two):
    if one == two:
        return EQUAL
    if one == [] and len(two) > 0:
        return SUBLIST
    if len(one) > 0 and two == []:
        return SUPERLIST
        
    s_one = '.'.join(str(i) for i in one) + '.'
    s_two = '.'.join(str(i) for i in two) + '.'
    
    if s_one in s_two and len(s_one) < len(s_two):
        return SUBLIST
    if s_two in s_one and len(s_one) > len(s_two):
        return SUPERLIST
    return UNEQUAL
