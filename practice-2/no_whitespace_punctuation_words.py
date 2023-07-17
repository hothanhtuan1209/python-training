"""
This module contains a code for exercises 13-1 related to:
Think Python, 2nd Edition
Chapter 13: Case Study: Data Structure Selection

Reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
"""

import string

def clean_word():
    """
    Reads a file and processes its content.

    print: list words
    """
    fin = open('test.txt')
    cleaned_words = []

    for line in fin:
        line = line.strip().split()

        for word in line:
            cleaned_word = ""
            
            for letter in word:
                if letter not in string.whitespace and letter not in string.punctuation:
                    cleaned_word += letter.lower()
            
            cleaned_words.append(cleaned_word)

    print(cleaned_words)

clean_word()
