"""
Uses set subtraction to find words in the book that are not in the word list.
"""


import os
from constants.constants import MARKOV_PATH, EBOOK_PATH
from helpers.file_reader import read_file


def find_word_notin_list(ebook_content, markov_content):
    """
    Find words in the ebook content that are not in the markov content.

    Parameters:
        - ebook_content (str): The content of the ebook file.
        - markov_content (str): The content of the markov file.

    Returns:
        - set: A set of words found in the ebook content but not in the
        markov content.
    """

    ebook_words = set(ebook_content.lower().split())
    markov_words = set(markov_content.lower().split())

    words_notin_list = ebook_words - markov_words

    print(words_notin_list)


def main():
    """
    Uses set subtraction to find words in the book that are not in the word
    list.
    """

    print(os.path.basename(__file__))
    content_of_markov = read_file(MARKOV_PATH)
    content_of_ebook = read_file(EBOOK_PATH)

    if content_of_markov and content_of_ebook:
        find_word_notin_list(content_of_ebook, content_of_markov)
