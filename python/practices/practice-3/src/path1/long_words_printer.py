"""
Read the words file and check the words, print the word if the word has more
than 20 letters excluding spaces
"""


import os
from helpers.file_reader import read_file_content
from constants.constant import word_file


def print_words(file_content):
    """
    Print words from a file that have a length greater than 20 characters.

    Args:
        - file_content (str): content of file word
    """

    lines = file_content.split('\n')
    for line in lines:
        word = line.strip()

        if len(word) > 20:
            print(word)


def main():
    """
    Check and print words with more than 20 letters from a word file
    """

    print(os.path.basename(__file__))
    file_content = read_file_content(word_file)

    if file_content:
        print_words(file_content)
