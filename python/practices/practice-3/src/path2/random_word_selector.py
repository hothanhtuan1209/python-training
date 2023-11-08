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
from constants.constants import EBOOK_PATH
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
            cleaned_word = word.strip(
                string.punctuation + string.whitespace
            ).lower()
            hist[cleaned_word] += 1

    return hist


def choose_random(hist):
    """
    Randomly select a word from a histogram based on word frequencies.

    Args:
        hist (dict): A histogram of word frequencies.

    Returns:
        str: A randomly selected word from the histogram. If the histogram
        is empty, it returns an empty string.
    """

    if not hist:
        return ''

    list_word = list(hist.keys())
    cumulative_sums = calculate_cumulative_sums(hist.values())
    total = cumulative_sums[-1]
    random_val = randint(0, total - 1)
    index = bisect(cumulative_sums, random_val)

    return list_word[index]


def calculate_cumulative_sums(elements):
    """
    Calculate the cumulative sum of the elements in a list.

    Args:
        elements (list): A list of integers.

    Returns:
        list: A list of cumulative sums of the input list.
    """

    total = 0
    cumulative_sums = []

    for element in elements:
        total += element
        cumulative_sums.append(total)

    return cumulative_sums


def main():
    """
    Reads an ebook file, processes it to choose a random word, and prints the
    word.
    """

    print(os.path.basename(__file__))
    file_content = read_file(EBOOK_PATH).splitlines()
    histogram = create_word_histogram(file_content)
    random_word = choose_random(histogram)

    print(random_word)
