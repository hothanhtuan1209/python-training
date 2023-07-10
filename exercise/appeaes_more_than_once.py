"""
This module contains a code for exercises 10-7 related to:
Think Python, 2nd Edition
Chapter 10: Lists

Takes a list and returns True if there is
any element that appears more than once.
"""

def has_duplicates():
    t = list(input('Enter list:'))
    set_t = set(t)
    """
    Input a list 

    Return True if list has any element appears more than once.
    """

    if len(t) == len(set_t):
        return False
    
    return True

print(has_duplicates())
