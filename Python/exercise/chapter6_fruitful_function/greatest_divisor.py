"""
The greatest common divisor (GCD) of a and b is the largest number that
divides both of them with no remainder.
One way to find the GCD of two numbers is based on the observation that if r
is the remainder when a is divided by b, then gcd a, b = gcd b,r .
As a base case, we can use gcd a, 0 = a.
"""


def gcd(a, b):
    """
    Find the greatest common divisor (GCD) of two numbers using the Euclidean
    algorithm.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The GCD of 'a' and 'b'.
    """

    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)


result = gcd(8, 12)
print(result)
