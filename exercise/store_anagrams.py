"""
This module contains a code for exercises 14-2 related to:
Think Python, 2nd Edition
Chapter 14: Files

imports anagram_sets and provides two new functions: store_anagrams should 
store the anagram dictionary in a “shelf ”; read_anagrams
should look up a word and return a list of its anagrams.
"""

import shelve

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

def store_anagrams(word_list_filename,dict_name):
    """
    Creates a dictionary of anagrams and stores it in a shelf.

    word_list_filename: Path to the file containing the word list.
    dict_name: Name to be given to the resulting dictionary shelf.
    """
    
    anagram_sets = find_anagrams(word_list_filename)

    with shelve.open(dict_name) as anagrams_dict:
        for i, anagram_set in enumerate(anagram_sets, 1):
            key = f'anagram_set_{i}'
            anagrams_dict[key] = anagram_set

def read_anagrams(word, dict_name):
    """
    Retrieves the list of anagrams for a given word from an existing anagrams dictionary.

    word: The word to be queried.
    dict_name: The name of the dictionary shelf.

    returns: A list of anagrams for the given word.
    """
    
    word_signature = signature(word)

    with shelve.open(dict_name) as anagrams_dict:
        key = word_signature
        return anagrams_dict.get(key, [])

word_list_filename = 'words.txt'
store_anagrams(word_list_filename,'anagram_dict.db')
print(read_anagrams('least', 'anagram_dict.db'))
