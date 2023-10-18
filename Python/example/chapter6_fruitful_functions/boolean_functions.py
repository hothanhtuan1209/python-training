def is_divisible(x, y):
    """
    Check if 'x' is divisible by 'y' and return True if it is, otherwise
    return False.

    Parameters:
        - x (int): The number to check for divisibility.
        - y (int): The divisor.

    Returns:
        - bool: True if 'x' is divisible by 'y', False otherwise.
    """

    if x % y == 0:
        return True
    else:
        return False
