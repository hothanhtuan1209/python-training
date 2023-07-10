"""
This module contains a code for exercises 10-1 related to:
Think Python, 2nd Edition
Chapter 10: Lists

The exercise asks you to calculate the sum of
all the elements in the list
"""

t = [[1, 2], [3], [4, 5, 6]]

def nested_sum(t):
    """
    Enter a list

    Return sum of list 
    """
    total = 0 
    
    for i in (t):
        total += sum(i)
    print(total)

nested_sum(t)
