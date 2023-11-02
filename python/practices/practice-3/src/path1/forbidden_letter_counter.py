"""
Count and print the number of words in a word list that do not contain
forbidden letters.
"""


import os


def avoids(words, letters):
    """
    Count the total number of words that do not contain any of the forbidden
    letters.
    """

    total = 0

    for word in words:
        if not any(letter in word for letter in letters):
            total += 1

    return total


def main():
    """
    Print the number of words in a word list that do not contain
    forbidden letters.
    """

    print(os.path.basename(__file__))
    words = input('Enter words separated by space:').split()
    letters = input('Enter a string of forbidden letters:')
    total = avoids(words, letters)

    print('Total words without forbidden letters:', total)
