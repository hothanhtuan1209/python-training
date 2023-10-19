def factorial(n):
    """
    Calculate and return the factorial of a non-negative integer 'n'.

    Parameters:
        - n (int): The non-negative integer for which to calculate the
        factorial.

    Returns:
        - int: The calculated factorial of 'n'.
    """

    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
    return result
