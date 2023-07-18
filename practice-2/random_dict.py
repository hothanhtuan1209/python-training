"""
This module contains a code for exercises 13-5 related to:
Think Python, 2nd Edition
Chapter 13: Case Study: Data Structure Selection

Write a function named choose_from_hist that takes a histogram as defined in 
“Dictionary as a Collection of Counters” on page 127 and returns a random value from
the histogram, chosen with probability in proportion to frequency.
"""

import random

def histogram(list_input):
    """
    Create 1 dictionary with letter as key and number of occurrences as value

    list_input: list

    return: dict
    """
    
    dict_hist = dict()
    
    for letter in list_input:
        if letter not in dict_hist:
            dict_hist[letter] = 1
        else:
            dict_hist[letter] += 1
    
    return dict_hist

def choose_from_hist(dict_hist):
    """
    Generate 1 list of keys based on occurrences

    dict_hist: dict
    """
    
    list_key = list()
    
    for key, value in dict_hist.items():
        for i in range(value):
            list_key.append(key)
    
    return random.choice(list_key)

list_input = ['a', 'a', 'b', 'c', 'c', 'd', 'c']
hist = histogram(list_input)

print(choose_from_hist(hist))
