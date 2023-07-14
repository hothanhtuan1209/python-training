"""
This module contains a code for exercises 12-2 related to:
Think Python, 2nd Edition
Chapter 12: Tuples

Reads a word list from a file (see “Reading Word Lists” on
page 99) and prints all the sets of words that are anagrams.
"""

def signature(word):
    """
    Returns the signature of a word.

    Signature is a string that contains all of the letters in order.

    word: string

    returns: string
    """
    
    return ''.join(sorted(word))

def find_anagrams(filename):
    """
    Finds all anagrams in a word list.

    filename: string filename of the word list

    returns: a list of lists of anagrams
    """
    
    anagram_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            word_signature = signature(word)

            # Add the word have same signature to the anagram dictionary
            if word_signature in anagram_dict:
                anagram_dict[word_signature].append(word)
            else:
                anagram_dict[word_signature] = [word]

    # Filter out sets of words with only one word
    anagram_sets = [word_list for word_list in anagram_dict.values() if len(word_list) > 1]

    return anagram_sets

def print_anagram_sets(anagram_sets):
    """
    Prints the sets of anagrams.

    anagram_sets: list of lists of anagrams
    """
    
    for anagram_set in anagram_sets:
        print(anagram_set)

word_file = "words.txt"
anagram_sets = find_anagrams(word_file)
print_anagram_sets(anagram_sets)
