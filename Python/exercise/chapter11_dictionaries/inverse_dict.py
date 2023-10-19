"""
This module contains a code for exercises 11-2 related to:
Think Python, 2nd Edition
Chapter 11: Dictionaries

This function reverses a dictionary and uses the dictionary's 
setdefault() method to generate key-value pairs.
"""

def invert_dict(dict_in):
    """
    Reverse the dictionaries, using the method setdefault()

    dict_in: dict

    return: reverse dict 
    """
    
    inverse = {}
    
    for key in dict_in:
        value = dict_in[key]
        inverse.setdefault(value, []).append(key)
    
    return inverse

print(invert_dict(dict_in={}))
