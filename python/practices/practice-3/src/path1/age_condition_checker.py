"""
This exercise's purpose is to find a number between 0 and 99,
that number, after adding 36, will be equal to its inverse.
"""


import os
from constants.constants import REVERSE_ADDITION_NUMBER


def check_condition_number(number):
    """
    This function returns a number if it adds 36 to its inverse

    Parameters:
        - number (string): a string of number to check condition.

    Returns:
        - string: the input number if it satisfies the condition,
        otherwise None.
    """

    list_of_digits = list(number)
    number_reverse = int(''.join(list_of_digits[::-1]))

    if int(number) + REVERSE_ADDITION_NUMBER == number_reverse:
        return number
    else:
        return None


def find_age_pairs():
    """
    Check each age from 0-99 to satisfy the condition of
    function check_condition_number

    Returns:
        - list: a list of numbers that satisfy the condition.
    """

    numbers = []
    for age in range(0, 100):
        string_of_age = str(age)
        padded_number = string_of_age.zfill(2)
        result = check_condition_number(padded_number)
        if result:
            numbers.append(result)

    return numbers


def main():
    """
    Find and print the numbers in the first 100 natural numbers such that
    adding 36 forms its inverse.
    """

    print(os.path.basename(__file__))
    numbers = find_age_pairs()

    for number in numbers:
        print(number)
