"""
Count and print percentage word in word list not contains the letter 'e' or 'E'
"""


import os


def count_words(words):
    """
    Count and calculate the percentage of words that do not contain 'E' or 'e'
    in a list of words.

    Parameters:
        - words: list of words input
    """

    words_has_no_e = 0

    for word in words:
        if 'e' not in word and 'E' not in word:
            print(word)
            words_has_no_e += 1

    return words_has_no_e


def percentage_words(words):
    """
    Calculate the percentage of words that do not contain 'E' or 'e'
    in a list of words

    Parameters:
        - words: list of words input
    """
    total_number_of_words = len(words)

    if total_number_of_words == 0:
        print("The word list is empty.")
        return

    words_has_no_e = count_words(words)
    percentage = (words_has_no_e / total_number_of_words) * 100

    print('Percentage of words without the letter e:', percentage)


def main():
    """
    Count and print percentage word in word list not contains the
    letter 'e' or 'E'
    """

    print(os.path.basename(__file__))
    words = input("Enter the list of words:").split()
    percentage_words(words)
