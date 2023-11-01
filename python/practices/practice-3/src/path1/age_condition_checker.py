"""
This exercise's purpose is to find a number between 0 and 99,
that number, after adding 36, will be equal to its inverse.
"""


import os


def check_condition_number(number):
    """
    This function prints a number if it adds 36 to its inverse

    Parameters:
        - number (int): a number to check condition.
    """

    list_of_digits = list(number)
    number_reverse = int(''.join(list_of_digits[::-1]))

    if int(number) + 36 == number_reverse:
        print(number)


def find_age_pairs():
    """
    Check each age from 0-99 to satisfy the condition of
    function check_condition_number
    """

    for age in range(0, 100):
        # Convert single-digit age to a two-character string
        string_of_age = str(age)
        padded_number = string_of_age.zfill(2)
        check_condition_number(padded_number)


def main():
    """
    Find and print the numbers in the first 100 natural numbers such that
    adding to 36 forms its inverse.
    """

    print(os.path.basename(__file__))
    find_age_pairs()
