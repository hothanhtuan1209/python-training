"""
This module contains a code for exercises 11-4 related to:
Think Python, 2nd Edition
Chapter 11: Dictionaries

Takes a list as a parameter and returns True if there is any object that appears more
than once in the list.
"""

def has_duplicates(list_input):
    """
    Check if there are any duplicate elements

    list_input: list

    return: True if list has any element appears more than once. 
    """
    
    count = {}
    
    for item in list_input:
        
        if item in count:
            return True
        count[item] = 1
    
    return False

has_duplicates()
