"""
Check the list of words to see if for each word the letters inside are in
alphabetical order
"""


import os


def check_abecedarian(word):
    """
    Check if a word is in alphabetical order.

    Parameters:
        word (str): The word to check for alphabetical order.

    Returns:
        bool: True if the word is in alphabetical order, False otherwise.
    """

    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False

    return True


def main():
    """
    Prints the words in the list with the letters in the words arranged
    in alphabetical order
    """

    list_word = input('Enter a list word:').split()
    count = 0

    for word in list_word:
        if check_abecedarian(word):
            count += 1

    print(os.path.basename(__file__))
    print('Abecedarian words:', count)
