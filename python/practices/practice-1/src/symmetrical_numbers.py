"""
This lesson goes through all 6 digit numbers, prints the numbers
with the last 4 or last 5 digits or all 6 numbers that are symmetrical.
"""


def is_palindrome(digits):
    """
    Check if a number represented by a list of digits is a palindrome.

    Parameters:
    digits (list): A list of digits representing the number.

    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """

    return digits == digits[::-1]


def check_odometer():
    """
    Check 6-digit numbers to find palindromic numbers among the last 4 digits,
    last 5 digits, and all 6 digits.
    """

    for number in range(100000, 1000000):
        digits = list(str(number))

        # Call function is_palindrome to check condition
        if (
            is_palindrome(digits[2:])
            or is_palindrome(digits[1:])
            or is_palindrome(digits)
        ):

            print(number)


check_odometer()
