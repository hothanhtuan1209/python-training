"""
This module contains a code for exercises 10-5 related to:
Think Python, 2nd Edition
Chapter 10: Lists

Takes a list as a parameter and returns True if
the list is sorted in ascending order and False otherwise.
"""

t = [1, 2, 3, 4, 5]

def is_sorted(t):
    """
    Input a list 't'

    Return True if the list is sorted and False otherwise
    """
    index = 0
    
    while index < len(t)-1:
        # Iterate over each element in the list 't'
        if t[index] > t[index+1]:
            return False
        else:
            index +=1

    return True

print(is_sorted(t))
