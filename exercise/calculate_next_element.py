"""
This module contains a code for exercises 10-2 related to:
Think Python, 2nd Edition
Chapter 10: Lists

This exercise requires entering a list and printing a 
new list with the i + n = i + (i + 1) + (i+2) +...+ (i+n-1)
"""

list_a = [5, 7, 9]

def cumsum(list_a):
    """
    Input: list_a

    Return list_b
    """
    sum = 0
    list_b = []
    
    for number in list_a:
        sum += number
        list_b.append(sum)
    
    return list_b

print(cumsum(list_a))
