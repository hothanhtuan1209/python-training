"""
This module contains a code for exercises 11-1 related to:
Think Python, 2nd Edition
Chapter 11: Dictionaries

Reads the words in words.txt and stores them as keys in
a dictionary. It doesn’t matter what the values are.
"""

def create_word_dictionary():
    """
    Returns a new dictionary that takes the words in the words.txt as keys

    return: dict
    """

    word_dictionary = {}
    read_file = open('words.txt')
    
    for line in read_file:
        word = line.strip()
        word_dictionary[word] = None
    
    return word_dictionary

create_word_dictionary()
