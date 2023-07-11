"""
This module contains a code for exercises 10-9 related to:
Think Python, 2nd Edition
Chapter 10: Lists

Reads the file words.txt and builds a list with one element per
word. Write two versions of this function, one using the append
method and the other using the idiom t = t + [x].

Download the word.txt file before running the program 
"""

def word_list_append():
    """"
    Get word list from file, using append function.

    return: list of string
    """

    word_list = []
    read_file = open('words.txt')

    for line in read_file:
        word = line.strip()
        word_list.append(word)
    
    return word_list

word_list_append()

def word_list_concatenate():
    """"
    Get word list from file, using the plus operator.

    return: list of string
    """

    word_list = []
    read_file = open('words.txt')

    for line in read_file:
        word = line.strip()
        word_list = word_list + [word]
    
    return word_list

word_list_concatenate()
