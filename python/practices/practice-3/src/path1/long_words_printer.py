"""
Read the words file and check the words, print the word if the word has more
than 20 letters excluding spaces
"""


import os
from helpers.file_reader import read_file
from constants.constants import WORD_PATH, WORD_LENGTH


def get_long_words(file_content):
    """
    Get words from a file that have a length greater than 20 characters.

    Args:
        - file_content (str): content of the word file.

    Returns:
        list: A list of words with more than 20 characters.
    """

    lines = file_content.split('\n')
    long_words = []

    for line in lines:
        word = line.strip()

        if len(word) > WORD_LENGTH:
            long_words.append(word)

    return long_words


def main():
    """
    Check and print words with more than number of WORD_LENGTH letter
    from a word file
    """

    print(os.path.basename(__file__))
    file_content = read_file(WORD_PATH)

    if file_content:
        long_words = get_long_words(file_content)

        for word in long_words:
            print(word)
