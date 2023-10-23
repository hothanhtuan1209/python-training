"""
This module contains a code for exercises 12-3 related to:
Think Python, 2nd Edition
Chapter 12: Tuples

Write a program that finds all of the metathesis pairs in the dictionary.
"""


def find_metathesis_pairs(filename):
    """
    Finds all metathesis pairs in the dictionary.

    filename: string filename of the dictionary

    returns: list of metathesis pairs
    """

    anagram_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip().lower()
            sorted_word = ''.join(sorted(word))

            if sorted_word in anagram_dict:
                for anagram in anagram_dict[sorted_word]:
                    if are_metathesis_pair(word, anagram):
                        return [(word, anagram)]

            else:
                anagram_dict[sorted_word] = [word]

    return []


def are_metathesis_pair(first_word, second_word):
    """
    Checks if two words form a metathesis pair.

    word1, word2: string

    returns: bool
    """

    if len(first_word) != len(second_word):
        return False

    # Count the number of different positions between the two words
    count = 0
    for i in range(len(first_word)):
        if first_word[i] != second_word[i]:
            count += 1

    return count == 2


word_list_file = "word_list.txt"
metathesis_pairs = find_metathesis_pairs(word_list_file)

for pair in metathesis_pairs:
    print(pair)
