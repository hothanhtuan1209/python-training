"""
This module contains a code for exercises 12-1 related to:
Think Python, 2nd Edition
Chapter 12: Tuples

Takes a string and prints the letters in
decreasing order of frequency.
"""

def most_frequent(string_input):
    """
    Sort by frequency of occurrence of characters

    string_input: string
    """
    
    frequency = {}
    
    for letter in string_input:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    
    char_freq_tuples = [(letter, frequency[letter]) for letter in frequency]
    sorted_tuples = sorted(char_freq_tuples, key=lambda x: x[1], reverse=True)
    
    for letter, freq in sorted_tuples:
        print(letter, freq)

most_frequent("Agility")
