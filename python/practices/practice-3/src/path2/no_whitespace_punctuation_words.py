"""
Reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
"""

import string
import os
from helpers.file_reader import read_file
from constants.constants import path_of_test_file


def clean_word(test):
    """
    Clean and process the content of a file.

    Parameters:
        - test (list of str): The lines of text to be cleaned.

    Returns:
        - list of str: A list of cleaned words.
    """

    cleaned_words = []

    for line in test:
        line = line.strip().split()

        for word in line:
            cleaned_word = ""

            for letter in word:
                if letter not in string.whitespace and letter not in string.punctuation:
                    cleaned_word += letter.lower()

            cleaned_words.append(cleaned_word)

    print(cleaned_words)


def main():
    """
    Clean and print words in file.
    """

    print(os.path.basename(__file__))
    file_content = read_file(path_of_test_file)

    if file_content:
        clean_word(file_content)
