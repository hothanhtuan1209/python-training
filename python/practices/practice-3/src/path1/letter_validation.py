"""
Enter a word and a string of letters, test the word using only the
letters in the string
"""


import os
from helpers.user_input import get_user_input


def uses_only(word, allowed_letter):
    """
    Check if a word contains only the specified letters.

    Parameters:
        - word (str): The word to check.
        - allowed_letter (str): A string containing the allowed letters.

    Returns:
        - bool: True if word contains only letters from string_letter,
        False otherwise.
    """

    for letter in word:
        if letter not in allowed_letter:
            return False

    return True


def main():
    """
    Enter a word and a string of letters, check whether the word only uses
    letters in the string or not
    """

    print(os.path.basename(__file__))
    word_input = get_user_input('Enter a word:')
    letters_input = get_user_input('Enter a string letters:')

    print(uses_only(word_input, letters_input))
