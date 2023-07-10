"""
This module contains a code for exercises 10-4 related to:
Think Python, 2nd Edition
Chapter 10: Lists

Takes a list, modifies it by removing the first and last
elements, and returns None.
"""

t = [1, 2, 3, 4, 5]

def chop(t):
    """
    input list 't'

    Return list 't' is removed the first and last element 
    """
    del t[:1]
    del t[-1:]
    print(t)

chop(t)
