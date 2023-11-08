"""
Read the words file and check the words, print the word if the word has more
than 20 letters excluding spaces
"""


import os
from helpers.file_reader import read_file
from constants.constants import WORD_PATH, WORD_LENGTH


def print_words(file_content):
    """
    Print words from a file that have a length greater
    than number of WORD_LENGTH.

    Args:
        - file_content (str): content of file word
    """

    lines = file_content.split('\n')
    for line in lines:
        word = line.strip()

        if len(word) > WORD_LENGTH:
            print(word)


def main():
    """
    Check and print words with more than number of WORD_LENGTH letter
    from a word file
    """

    print(os.path.basename(__file__))
    file_content = read_file(WORD_PATH)

    if file_content:
        print_words(file_content)
