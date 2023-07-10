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
    Print list after removing the first and last characters of the list
    Take in a list have name 'list_input'

    print 'list_input' after remove the first and last element 
    """

    del list_input[:1]
    del list_input[-1:]
    print(list_input)

chop(list_input)
