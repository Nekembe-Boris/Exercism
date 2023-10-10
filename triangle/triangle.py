def equilateral(sides):
    """An _equilateral_ triangle has all three sides the same length"""
    return checker(sides) and len(set(sides)) == 1


def isosceles(sides):
    """An _isosceles_ triangle has at least two sides the same length."""
    return checker(sides) and len(set(sides)) <= 2



def scalene(sides):
    """A _scalene_ triangle has all sides of different lengths."""
    return checker(sides) and len(set(sides)) == 3




def checker(sides):
    """Checks if any side is 0 or if the sides violate the triangle_inequality rule """
    if (sort_sides := sorted(sides))[0] > 0:
        if sum(sort_sides[:2]) >= sort_sides[2]:
            return True
    return False
