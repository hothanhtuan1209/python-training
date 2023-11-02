"""
Check and prints words containing three consecutive double letters
"""


import os


def is_triple_double(word):
    """
    Check if a word contains three consecutive double letters.

    Parameters:
        - word (str): The input word to check.

    Returns:
        - bool: True if the word contains three consecutive double letters,
        False otherwise.
    """

    i = 0

    while i < len(word) - 5:
        if (
            word[i] == word[i + 1]
            and word[i + 2] == word[i + 3]
            and word[i + 4] == word[i + 5]
        ):
            return True
        i += 1

    return False


def find_triple_double():
    """
    Prints words with triple double letters from word list.
    """

    fin = open('words.txt', encoding='utf-8')

    for line in fin:
        word = line.strip()

        if is_triple_double(word):
            print(word)


def main():
    """
    Prints words containing three consecutive double letters
    """

    print(os.path.basename(__file__))
    find_triple_double()
