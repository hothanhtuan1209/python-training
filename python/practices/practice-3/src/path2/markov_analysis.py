"""
Write a program to read a text from a file and perform Markov analysis. The
result should be a dictionary that maps from prefixes to a collection of
possible suffixes.
"""


import os
import collections
from constants.constants import EBOOK, TOP_COUNT
from helpers.content_cleaner import clean_words
from helpers.file_reader import read_file


def count_words(cleaned_words):
    """
    Count the occurrences of each word in a list of cleaned words and sort
    them by frequency.

    Args:
        - cleaned_words (list of str): A list of cleaned words.

    Returns:
        - dict: A dictionary where keys are unique words and values are their
        frequencies.
    """

    word_counts = collections.Counter(cleaned_words)
    sorted_word_counts = dict(
        sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    )

    return sorted_word_counts


def print_top_words(ebook_text):
    """
    Read a text file, clean the words, and print the 20 most frequently
    used words in the ebook.

    Args:
        - ebook_text (str): The content of the ebook.

    Returns:
        None
    """
    cleaned_words = clean_words(ebook_text)
    total_number_of_words = count_words(cleaned_words)

    top_count = TOP_COUNT

    for i, (word, count) in enumerate(total_number_of_words.items()):
        print(i + 1, word, count)
        if i + 1 == top_count:
            break


def main():
    """
    Print the 20 most frequently used words in the ebook.
    """

    print(os.path.basename(__file__))
    ebook_text = read_file(EBOOK)
    print_top_words(ebook_text)
