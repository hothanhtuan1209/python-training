"""
Reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
"""


import os
from helpers.file_reader import read_file
from constants.constants import TEST


def clean_and_split_text(test):
    """
    Cleans and splits a text into words, removing whitespace and punctuation.

    Parameters:
        test (str): A string containing the text to process.

    Returns:
        list: A list of cleaned and split words.
    """

    cleaned_text = ''.join(
        char.lower() if char.isalnum() or char.isspace() else ' '
        for char in test
    )

    cleaned_words = [word for word in cleaned_text.split() if word]

    return cleaned_words


def main():
    """
    Reads a text file, cleans it, and prints the cleaned words.
    """

    print(os.path.basename(__file__))
    file_content = read_file(TEST)

    if file_content:
        cleaned_words = clean_and_split_text(file_content)
        for word in cleaned_words:
            print(word)
