"""
This module contains a code for exercises 11-3 related to:
Think Python, 2nd Edition
Chapter 11: Dictionaries

Memoize the Ackermann function from Exercise 6-2 and see if memoization makes it
possible to evaluate the function with bigger arguments.
"""

dict_variable = {}

def ackermann(m, n):
    """
    Computes the Ackermann function 

    n, m: non-negative integers

    return: integers
    """
    
    if m == 0:
        return n+1
    
    if n == 0:
        return ackermann(m-1, 1)
    
    if (m, n) in dict_variable:
        return dict_variable[m, n]
    
    else:
        dict_variable[m, n] = ackermann(m-1, ackermann(m, n-1))
        return dict_variable[m, n]


print(ackermann(3, 4))
