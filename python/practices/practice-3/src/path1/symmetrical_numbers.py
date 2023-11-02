"""
Check and prints the numbers with the last 4 or last 5 digits or all 6 numbers
that are symmetrical.
"""


import os


def reverse_digits(digits):
    """
    Reverse a list of digits

    Parameters:
        digits (list): A list of digits representing the number.

    Returns:
        Returns a list that has been reversed compared to the original list
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
            reverse_digits(list_of_digits[2:])
            or reverse_digits(list_of_digits[1:])
            or reverse_digits(list_of_digits)
        ):
            print(number)


def main():
    """
    Prints the numbers with the last 4 or last 5 digits or all 6
    numbers that are symmetrical.
    """

    print(os.path.basename(__file__))
    check_palindrome()
