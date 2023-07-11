"""
This module contains a code for exercises 10-11 related to:
Think Python, 2nd Edition
Chapter 10: Lists

Two words are a “reverse pair” if each is the reverse of the other.
Write a program that finds all the reverse pairs in the word list.
"""

def reverse_pair():
    """
    Enter a Word list from keyboard, and find the words that are the reverse.

    print list of string
    """

    word_list = input('Enter a word list:').split()
    reverse_word_list = []

    for word in word_list:
        reverse_word = word[::-1]
        
        if reverse_word in word_list  and word != reverse_word:
            # Add pairs of elements to the new list
            reverse_word_list.append((word,reverse_word))            
        
    print(reverse_word_list)    

reverse_pair()
