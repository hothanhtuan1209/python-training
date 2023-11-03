"""
Check and prints the numbers with the last 4 or last 5 digits or all 6 numbers
that are symmetrical.
"""


import os


def is_symmetric(digits):
    """
    Check if a list of digits is symmetric.

    Parameters:
        digits (list): A list of digits to check for symmetry.

    Returns:
        bool: True if the list of digits is symmetric
    """

    return digits == digits[::-1]


def check_palindrome():
    """
    Check and print 6-digit numbers to find palindromic numbers among the last
    4 digits, last 5 digits, and all 6 digits.
    """

    for number in range(100000, 1000000):
        list_of_digits = list(str(number))

        if (
            is_symmetric(list_of_digits[2:])
            or is_symmetric(list_of_digits[1:])
            or is_symmetric(list_of_digits)
        ):
            print(number)


def main():
    """
    Prints the numbers with the last 4 or last 5 digits or all 6
    numbers that are symmetrical.
    """

    print(os.path.basename(__file__))
    check_palindrome()
