"""
Prints all the words in the book that are not in the word list.
Reads the content of the ebook file and the word list file, and then finds and
prints all the words from the ebook that do not appear in the word list.
"""


import os
from constants.constants import EBOOK, WORD
from helpers.file_reader import read_file


def extract_words_from_content(content):
    """
    Extracts words from a content string and returns a list of words.

    Args:
        content (str): The content string containing words.

    Returns:
        list: A list of words extracted from the content.
    """

    word_list = []

    for word in content.split():
        cleaned_word = word.strip()

        if cleaned_word:
            word_list.append(cleaned_word)

    return word_list


def find_missing_words(book_content, words_content):
    """
    Finds all words in book file that do not appear in words file.

    book_filename: string, name of the test file
    words_filename: string, name of the words file

    returns: list of missing words
    """

    test_words = extract_words_from_content(book_content)
    words_list = extract_words_from_content(words_content)
    missing_words = []

    for word in test_words:
        if word not in words_list:
            missing_words.append(word)

    return missing_words


def main():
    """
    Find and print words from the ebook that are not in the word list.
    """

    print(os.path.basename(__file__))
    book_content = read_file(EBOOK)
    words_content = read_file(WORD)

    missing_words = find_missing_words(book_content, words_content)

    for word in missing_words:
        print(word)
