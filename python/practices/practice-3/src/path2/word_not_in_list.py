"""
Prints all the words in the book that are not in the word list.
Reads the content of the ebook file and the word list file, and then finds and
prints all the words from the ebook that do not appear in the word list.
"""


import os
from constants.constants import EBOOK_PATH, WORD_PATH
from helpers.file_reader import read_file


def extract_words(content):
    """
    Extracts words from a content string and returns a list of words.

    Args:
        content (str): The content string containing words.

    Returns:
        list: A list of words extracted from the content.
    """

    word_list = []

    word_list = [word.strip() for word in content.split() if word.strip()]

    return word_list


def find_missing_words(book_content, words_content):
    """
    Find words in the book_content that do not appear in the words_content.

    Args:
        book_content (str): The content of the book, as a string.
        words_content (str): The content of the words file, as a string.

    Returns:
        list: A list of missing words found in the book_content but not in the
              words_content.
    """

    test_words = extract_words(book_content)
    words_list = extract_words(words_content)
    missing_words = []

    missing_words = [word for word in test_words if word not in words_list]

    return missing_words


def main():
    """
    Find and print words from the ebook that are not in the word list.
    """

    print(os.path.basename(__file__))
    book_content = read_file(EBOOK_PATH)
    words_content = read_file(WORD_PATH)

    missing_words = find_missing_words(book_content, words_content)

    for word in missing_words:
        print(word)
