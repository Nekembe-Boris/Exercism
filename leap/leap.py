"""Function for checking if a year is a leap year"""
def leap_year(year):
    """Checks if year is a leap year"""
    if year % 4 == 0:
        if year % 100 != 0:
            return True

        if year % 400 == 0:
            return True
    return False
