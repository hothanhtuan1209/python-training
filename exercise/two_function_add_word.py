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
    Get word in word.txt file, remove spaces and add to new list 

    return: new word list using 'append' to add word from flie 
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
    Get word in word.txt file, remove spaces and add to new list 

    return: new word list using the idiom word_list = word_list + [word] to add word from file
    """

    word_list = []
    read_file = open('words.txt')

    for line in read_file:
        word = line.strip()
        word_list = word_list + [word]
    
    return word_list

word_list_concatenate()
