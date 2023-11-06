"""
Takes in a list of words and a string of characters, checks and counts the
words using all the characters in the string and prints the result.
"""


import os
from helpers.user_input import get_user_input


def uses_all(word, required_letters):
    """
    Check if a word contains all the required letters.

    Parameters:
        - word (str): The word to check.
        - required_letters (str): A string containing the letters that must be
        present in the word.

    Returns:
        - bool: True if the word contains all the required letters, False
        otherwise.
    """

    for letter in required_letters:
        if letter not in word:
            return False

    return True


def count_words(words, required_letters):
    """
    Count the number of words in a list that contain all the required letters.

    Parameters:
        - words (list): A list of words to be checked.
        - required_letters (str): A string containing the letters that must be
          present in each word.

    Returns:
        - int: The count of words that contain all the required letters.
    """

    count = 0

    for word in words:
        if uses_all(word, required_letters):
            count += 1

    return count


def main():
    """
    Check and print all word that uses all the letters in a string
    """

    print(os.path.basename(__file__))
    words = get_user_input("Enter a list of words: ").split()
    required_letters = get_user_input("Enter a string required letters:")
    print(count_words(words, required_letters))
