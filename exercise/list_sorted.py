"""
This module contains a code for exercises 10-5 related to:
Think Python, 2nd Edition
Chapter 10: Lists

Takes a list as a parameter and returns True if
the list is sorted in ascending order and False otherwise.
"""

list_input = [1, 2, 3, 4, 5]

def is_sorted(list_input):
    """
    Enter a list 'list_input'

    return: True if the list is sorted and False otherwise
    """

    index = 0
    
    while index < len(list_input)-1:
        # Iterate over each element in the list 'list_input'
        if list_input[index] > list_input[index+1]:
            return False
        else:
            index +=1

    return True

print(is_sorted(list_input))
