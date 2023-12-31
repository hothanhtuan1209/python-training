"""
This module contains a code for exercises 10-1 related to:
Think Python, 2nd Edition
Chapter 10: Lists

The exercise asks you to calculate the sum of
all the elements in the list
"""


list_input = [[1, 2], [3], [4, 5, 6]]


def nested_sum(list_input):
    """
    Sum the elements in the list, including the nested list
    """

    total = 0

    for i in (list_input):
        total += sum(i)

    print(total)


nested_sum(list_input)
