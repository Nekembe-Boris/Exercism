"""Script contains STEP function that proves the Collatz Conjecture"""

def steps(number):
    """This function returns the number of times it takes for a number to be divided timm it reaches 1"""
    
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        times = 0

        while number != 1:

            result = 0
            if number % 2 == 0:
                result = number/2
                times += 1
            else:
                result = (3 * number) + 1
                times += 1
            number = result

    return times


me = steps(12)
print(me)