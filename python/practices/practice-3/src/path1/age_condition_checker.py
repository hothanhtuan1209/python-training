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


def reverse_age():
    """
    Check each age from 0-99 to satisfy the condition of
    function check_condition_number
    """

    for age in range(0, 100):
        # Convert all 1 digit ages to 2 character strings
        string_of_digits_age = str(age).zfill(2)
        check_condition_number(string_of_digits_age)


def main():
    """
    It calls the 'reverse_age' function to check each number from 0 to 99 for
    satisfying the condition specified in the
    'check_condition_number' function.
    """

    print(os.path.basename(__file__))
    reverse_age()
