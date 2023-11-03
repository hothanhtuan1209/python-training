"""
Check and prints words containing three consecutive double letters
"""


import os


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


def find_triple_double():
    """
    Prints words with triple double letters from word list.
    """

    fin = open('words.txt', encoding='utf-8')

    for line in fin:
        word = line.strip()

        if contains_three_double(word):
            print(word)


def main():
    """
    Prints words containing three consecutive double letters
    """

    print(os.path.basename(__file__))
    find_triple_double()
