"""
This module contains a code for exercises 10-7 related to:
Think Python, 2nd Edition
Chapter 10: Lists

Takes a list and returns True if there is
any element that appears more than once.
"""


def has_duplicates():
    """
    Check if there are any duplicate elements

    Enter a list from keyboard

    return: True if list has any element appears more than once.
    """

    list_input = list(input('Enter list:'))
    set_list_input = set(set_list_input)

    if len(list_input) == len(set_list_input):
        return False

    return True


print(has_duplicates())
