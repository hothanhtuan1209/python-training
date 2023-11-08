"""
Count and print the number of words in a word list that do not contain
forbidden letters.
"""


import os


def avoids(word, letters):
    """
    Check if a word does not contain any of the forbidden letters.

    Parameters:
        - word (str): The word to check.
        - letters (str): A string of forbidden letters.

    Returns:
        - bool: True if the word does not contain any forbidden letters,
        False otherwise.
    """

    return all(letter not in word for letter in letters)


def count_avoided_words(words, letters):
    """
    Count the total number of words that do not contain any of the forbidden
    letters.

    Parameters:
        - words (list): A list of words.
        - letters (str): A string of forbidden letters.

    Returns:
        - int: The total number of words without forbidden letters.
    """

    return sum(1 for word in words if avoids(word, letters))


def main():
    """
    Print the number of words in a word list that do not contain
    forbidden letters.
    """

    print(os.path.basename(__file__))
    words = input('Enter words separated by space:').split()
    letters = input('Enter a string of forbidden letters:')
    total = count_avoided_words(words, letters)

    print('Total words without forbidden letters:', total)
