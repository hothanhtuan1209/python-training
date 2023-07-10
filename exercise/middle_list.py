"""
This module contains a code for exercises 10-3 related to:
Think Python, 2nd Edition
Chapter 10: Lists

Takes a list and returns a new list that contains all
but the first and last elements.
"""

t = [1, 2, 3, 4, 5, 6, 7]

def middle(t):
    """
    Input list 't'

    Take elements have index 1 to index len(1)-1 from 't' add to new_list
    """
    new_list = t[1:(len(t)-1)]
    print(new_list)

middle(t)
