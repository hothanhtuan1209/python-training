"""
This module contains a code for exercises 10-3 related to:
Think Python, 2nd Edition
Chapter 10: Lists

Takes a list and returns a new list that contains all
but the first and last elements.
"""

list_input = [1, 2, 3, 4, 5, 6, 7]

def middle(list_input):
    """
    Enter a list have name 'add a detailed description of the function'

    Take elements have index 1 to index len(1)-1 from 'list_input' add to new_list
    """
    
    new_list = list_input[1:(len(list_input)-1)]
    print(new_list)

middle(list_input)