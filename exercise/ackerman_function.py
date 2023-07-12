"""
This module contains a code for exercises 11-3 related to:
Think Python, 2nd Edition
Chapter 11: Dictionaries

Memoize the Ackermann function from Exercise 6-2 and see if memoization makes it
possible to evaluate the function with bigger arguments.
"""

dict_variable = {}

def ackermann(second_number, first_number):
    """
    Computes the Ackermann function 

    first_number, second_number: non-negative integers

    return: integers
    """
    
    if second_number == 0:
        return first_number+1
    
    if first_number == 0:
        return ackermann(second_number-1, 1)
    
    if (second_number, first_number) in dict_variable:
        return dict_variable[second_number, first_number]
    
    else:
        dict_variable[second_number, first_number] = ackermann(second_number-1, ackermann(second_number, first_number-1))
        return dict_variable[second_number, first_number]

print(ackermann(3, 4))
