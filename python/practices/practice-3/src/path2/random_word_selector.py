"""
This program randomly selects a word from a given ebook. It cleans and
processes the text, creating a histogram of word frequencies. Then, it selects
a random word with a probability proportional to its frequency.
"""


import string
import collections
import os
from random import randint
from bisect import bisect
from constants.constants import EBOOK
from helpers.file_reader import read_file


def create_word_histogram(text_lines):
    """
    Create a word histogram from a list of text lines.

    Args:
        text_lines (list): A list of text lines to process.

    Returns:
        dict: A histogram where keys represent cleaned words, and values
        represent word frequencies.
    """

    hist = collections.Counter()

    for line in text_lines:
        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace).lower()
            hist[word] = hist.get(word, 0) + 1

    return hist


def calculate_cumulative_sums(elements):
    """
    Calculate the cumulative sum of the elements in a list.

    Args:
        elements (list): A list of integers.

    Returns:
        list: A list of cumulative sums of the input list.
    """

    total = 0
    for i in range(len(elements)):
        total += elements[i]
        elements[i] = total

    return elements


def choose_random(hist):
    """
    Randomly generate a number and get the letter corresponding to that number

    Args:
        hist (dict): A histogram of word frequencies.

    Returns:
        str: A randomly selected word from the histogram.
    """

    list_word = list(hist.keys())
    cumulative_sums = calculate_cumulative_sums(
        list(int(i) for i in hist.values())
    )

    total = cumulative_sums[-1]

    if total > 0:
        random_val = randint(0, total - 1)
        index = bisect(cumulative_sums, random_val)

        return list_word[index]

    else:
        return None


def main():
    """
    Reads an ebook file, processes it to choose a random word, and prints the
    word.
    """

    print(os.path.basename(__file__))
    file_content = read_file(EBOOK).splitlines()
    print(choose_random(create_word_histogram(file_content)))
