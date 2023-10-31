"""
Write a program that reads words.txt and prints only the words with more than
20 characters (not counting whitespace).
"""


def print_words(file):
    """
    Print words from a file that have a length greater than 20 characters.

    Args:
        - file (str): The path to the input file containing a list of words.
    """

    fin = open(file, encoding='utf-8')

    for line in fin:
        word = line.strip()

        if len(word) > 20:
            print(word)


print_words('words.txt')
