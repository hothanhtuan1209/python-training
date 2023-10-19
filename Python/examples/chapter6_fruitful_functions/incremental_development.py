import math


def distance(x1, y1, x2, y2):
    """
    Calculate and return the Euclidean distance between two points (x1, y1)
    and (x2, y2).

    Parameters:
        - x1 (float): x-coordinate of the first point.
        - y1 (float): y-coordinate of the first point.
        - x2 (float): x-coordinate of the second point.
        - y2 (float): y-coordinate of the second point.

    Returns:
        - float: The calculated Euclidean distance between the two points.
    """

    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result
