"""
Enter a word and a string of letters, test the word using only the
letters in the string
"""


import os


def used_only_letters(word, string_letter):
    """
    Check if a word contains only the specified letters.

    Parameters:
        - word (str): The word to check.
        - string_letter (str): A string containing the allowed letters.

    Returns:
        - bool: True if 'word' contains only letters from 'string_letter',
        False otherwise.
    """

    for letter in word:
        if letter not in string_letter:
            return False

    return True


def main():
    """
    Enter a word and a string of letters, check whether the word only uses
    letters in the string or not
    """

    print(os.path.basename(__file__))
    word = input('Enter a word:')
    string_letters = input('Enter a string letters:')

    print(used_only_letters(word, string_letters))
