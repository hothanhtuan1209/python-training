"""
Count and print percentage word in word list not contains the letter 'e' or 'E'
"""


import os


def count_words(words):
    """
    Count and calculate the percentage of words that do not contain 'E' or 'e'
    in a list of words.
    """

    total_number_of_words = len(words)
    words_has_no_e = 0

    for word in words:
        if 'e' not in word and 'E' not in word:
            print(word)
            words_has_no_e += 1

    percentage = (words_has_no_e/total_number_of_words) * 100
    print('Percentage of words without the letter e', percentage)


def main():
    """
    Count and print percentage word in word list not contains the
    letter 'e' or 'E'
    """

    print(os.path.basename(__file__))
    words = input("Enter the list of words: ").split()
    count_words(words)
