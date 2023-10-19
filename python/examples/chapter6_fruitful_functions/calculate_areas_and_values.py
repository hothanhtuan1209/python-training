import math


def area(radius):
    """
    Calculate and return the area of a circle with the given radius.

    Parameters:
        - radius (float): The radius of the circle.

    Returns:
        - float: The calculated area of the circle.
    """

    a = math.pi * radius**2
    return a


def absolute_value(x):
    """
    Calculate and return the absolute value of a number.

    Parameters:
        - x (float): The number for which to calculate the absolute value.

    Returns:
        - float: The absolute value of the input number 'x'.
    """

    if x < 0:
        return -x
    else:
        return x
