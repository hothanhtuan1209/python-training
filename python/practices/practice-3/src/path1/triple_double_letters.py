"""
Check and prints words containing three consecutive double letters
"""


import os
from helpers.file_reader import read_file
from constants.constants import WORD_PATH


def contains_three_double(word):
    """
    Check if a word contains three consecutive double letters.

    Parameters:
        - word (str): The input word to check.

    Returns:
        - bool: True if the word contains three consecutive double letters,
        False otherwise.
    """

    index = 0

    while index < len(word) - 5:
        if (
            word[index] == word[index + 1]
            and word[index + 2] == word[index + 3]
            and word[index + 4] == word[index + 5]
        ):
            return True
        index += 1

    return False


def find_triple_double(file_content):
    """
    Prints words with triple double letters from word list.

    Parameters:
        - file_content (str): The content of the word list.

    Returns:
        None
    """

    if file_content:
        lines = file_content.split('\n')

        for line in lines:
            word = line.strip()

            if contains_three_double(word):
                print(word)


def main():
    """
    Main function to print words containing three consecutive double letters.
    """
    print(os.path.basename(__file__))
    file_content = read_file(WORD_PATH)
    find_triple_double(file_content)
