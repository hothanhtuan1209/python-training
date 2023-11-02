"""
Count and print the number of words in a word list that do not contain
forbidden letters.
"""


import os


def avoids():
    """
    Count the total number of words that do not contain any of the forbidden
    letters.
    """

    words = input('Enter words separated by space:').split()
    letters = input('Enter a string of forbidden letters:')

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

    total = avoids()
    print(os.path.basename(__file__))
    print('Total words without forbidden letters:', total)
