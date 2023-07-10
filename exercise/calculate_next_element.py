"""
This module contains a code for exercises 10-2 related to:
Think Python, 2nd Edition
Chapter 10: Lists

This exercise requires entering a list and printing a 
new list with the i + n = i + (i + 1) + (i+2) +...+ (i+n-1)
"""

list_input = [5, 7, 9]

def cumsum(list_input):
    """
    Take in a number list 'lits_input"

    return: List_output have elements are calculated from the elements of list_input 
    """

    sum = 0
    list_output = []
    
    for number in list_input:
        sum += number
        list_output.append(sum)
    
    return list_output

print(cumsum(list_input))
