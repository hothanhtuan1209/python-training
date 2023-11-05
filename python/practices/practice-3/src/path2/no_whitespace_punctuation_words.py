"""
Reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
"""


import string
import os
from helpers.file_reader import read_file
from constants.constants import path_of_test_file


def clean_text_and_split(test):
    """
    Cleans and splits a text into words.

    Parameters:
        test (list): A list of text lines to process.

    Returns:
        list: A list of cleaned and split words.
    """
    cleaned_words = []

    for line in test:
        line = line.strip()

        if line:
            words = line.split()

            for word in words:
                cleaned_word = "".join(
                    letter.lower() for letter in word if letter not in string.whitespace and letter not in string.punctuation
                )
                cleaned_words.append(cleaned_word)

    return cleaned_words


def main():
    """
    Process a text file, clean and split its content into words, and print
    the result.
    """

    print(os.path.basename(__file__))
    file_content = read_file(path_of_test_file)

    if file_content:
        cleaned_words = clean_text_and_split(file_content)

        for word in cleaned_words:
            print(word)
