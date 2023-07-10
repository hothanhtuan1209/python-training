"""
This module contains a code for exercises 10-6 related to:
Think Python, 2nd Edition
Chapter 10: Lists

Two words are anagrams if you can rearrange the letters
from one to spell the other. Takes two strings and returns True if they are anagrams.
"""

def is_anagram():
    """
    Check if one word is the reverse of the other

    Enter 2 words from keyboard.
    
    returns: True if anagram, False for otherwise
    """
    
    first_word = list(input('Enter first word:'))
    second_word = list(input('Enter second word :'))
    
    if first_word == second_word[::-1]:
        return True
    else:
        return False

print(is_anagram())
