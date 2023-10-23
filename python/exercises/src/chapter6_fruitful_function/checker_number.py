"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b.
Write a function called is_power that takes parameters a and b and returns True
if a is a power of b. Note: you will have to think about the base case.
"""


def checknumber(a, b):
    """
    Check if a number 'a' is divisible by 'b' and the result of the division
    'a/b' is also divisible by 'b'.

    Parameters:
        a (int): The number to be checked for divisibility.
        b (int): The divisor to check against.

    Returns:
        bool: True if 'a' is divisible by 'b' and 'a/b' is divisible by 'b',
        False otherwise.
    """

    if a % b == 0 and (a/b) % b == 0:
        return True
    else:
        return False


result = checknumber(9, 3)
print(result)
