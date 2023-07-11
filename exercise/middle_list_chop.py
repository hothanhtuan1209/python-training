"""
This module contains a code for exercises 10-4 related to:
Think Python, 2nd Edition
Chapter 10: Lists

Takes a list, modifies it by removing the first and last
elements, and returns None.
"""

list_input = [1, 2, 3, 4, 5]

def chop(list_input):
    """
    Remove the first and last items from the list.

    list_input: list of int
    """

    del list_input[:1]
    del list_input[-1:]
    print(list_input)

chop(list_input)
