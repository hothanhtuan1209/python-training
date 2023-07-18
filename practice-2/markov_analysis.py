"""
This module contains a code for exercises 13-8 related to:
Think Python, 2nd Edition
Chapter 13: Case Study: Data Structure Selection

Write a program to read a text from a file and perform Markov analysis. The
result should be a dictionary that maps from prefixes to a collection of possible
suffixes.

Download markov.txt file
"""

import random

def read_text(filename):
    """
    Reads a text from a file and returns it as a string.
    
    returns: string
    """
    
    with open(filename, 'r',encoding = 'utf-8') as file:
        text = file.read()
    
    return text

def markov_analysis(text, prefix_length):
    """
    Performs Markov analysis on the given text.

    text: string
    prefix_length: int

    returns: dict
    """
    
    prefixes = {}
    words = text.split()

    for i in range(len(words) - prefix_length):
        prefix = tuple(words[i:i+prefix_length])
        suffix = words[i+prefix_length]
        
        if prefix in prefixes:
            prefixes[prefix].append(suffix)
        else:
            prefixes[prefix] = [suffix]
    
    return prefixes

def random_markov(prefixes, prefix_length, num_words):
    """
    Randomly generate 1 text from the dictionary

    prefixes: dict

    returns: string
    """
    
    random_text = ''
    prefix_list = list(random.choice(list(prefixes.keys())))

    for _ in range(num_words):
        prefix = tuple(prefix_list[-prefix_length:])
        
        if prefix in prefixes:
            suffix = random.choice(prefixes[prefix])
            random_text += suffix + ' '
            prefix_list.append(suffix)
        else:
            break

    return random_text.strip()

num_words = 50
prefix_length = 5
filename = 'markov.txt'
text = read_text(filename)
print(markov_analysis(text, prefix_length))

prefixes = markov_analysis(text, prefix_length)
random_text = random_markov(prefixes, prefix_length, num_words)
print(random_text)
