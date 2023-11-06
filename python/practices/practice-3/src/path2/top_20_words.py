"""
Read a text file, clean the words, and print the 20 most frequently used words
in the ebook. This script reads the content of an ebook from a specified file,
cleans the words by removing punctuation and converting them to lowercase, and
then counts and prints the 20 most frequently used words in the ebook.
"""


import os
import collections
from constants.constants import EBOOK
from helpers.file_reader import read_file


def clean_words(text):
    """
    Clean a text by removing punctuation, converting words to lowercase,
    and counting the frequency of each word.

    Args:
        - text (str): The input text to be processed.

    Returns:
        - list of str: A list of cleaned words without punctuation and in
        lowercase.

    """

    cleaned_words = []

    for line in text:
        words = line.strip().split()

        for word in words:
            cleaned_word = "".join(c.lower() for c in word if c.isalnum())
            if cleaned_word:
                cleaned_words.append(cleaned_word)

    return cleaned_words


def count_words(cleaned_words):
    """
    Count the occurrences of each word in a list of cleaned words and sort
    them by frequency.

    Args:
        - cleaned_words (list of str): A list of cleaned words.

    Returns:
        - dict: A dictionary where keys are unique words and values are their
        frequencies.

    """

    word_counts = collections.Counter(cleaned_words)
    sorted_word_counts = dict(
        sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        )

    return sorted_word_counts


def main():
    """
    Read a text file, clean the words, and print the 20 most frequently
    
    used words in the ebook.
    """

    print(os.path.basename(__file__))
    ebook_text = read_file(EBOOK)
    cleaned_words = clean_words(ebook_text)
    word_counts = count_words(cleaned_words)

    top_count = 20
    for i, (word, count) in enumerate(word_counts.items()):
        print(i + 1, word, count)
        if i + 1 == top_count:
            break
