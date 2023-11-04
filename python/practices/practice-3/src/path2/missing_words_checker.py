"""
Uses set subtraction to find words in the book that are not in the word list.
"""


import os
from constant.constant_file import markov_file, ebook_file
from helpers.file_reader import read_file_content


def find_word_notin_list(file_ebook, file_markov):
    """
    Find words in the ebook content that are not in the markov content.

    Parameters:
        ebook_content (set): The set of words in the ebook content.
        markov_content (set): The set of words in the markov content.

    Returns:
        set: A set of words found in the ebook content but not in the markov
        content.
    """

    ebook_content = set(file_ebook.read().lower().split())
    markov_content = set(file_markov.read().lower().split())

    words_notin_list = ebook_content - markov_content

    print(words_notin_list)


def main():
    """
    Uses set subtraction to find words in the book that are not in the word
    list.
    """

    print(os.path.basename(__file__))
    content_of_markov = read_file_content(markov_file)
    content_of_ebook = read_file_content(ebook_file)

    if content_of_markov and content_of_ebook is not None:
        find_word_notin_list(content_of_ebook, content_of_markov)
