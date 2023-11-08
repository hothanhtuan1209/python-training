"""
Write a program that reads a text from a file, counts word frequencies, and
prints one line for each word, in descending order of frequency, with
log f and log r.
"""


import os
import string
import math
import collections
from helpers.file_reader import read_file
from constants.constants import MARKOV


def count_word_frequencies(text):
    """
    Counts the frequencies of words in the given text.

    Parameters:
        - text (str): A string containing the text to analyze.

    Returns:
        - collections.Counter: A Counter object with word frequencies.
    """

    hist = collections.Counter()
    words = text.split()

    for word in words:
        word = word.strip(string.punctuation + string.whitespace).lower()
        hist[word] += 1

    return hist


def calculate_log_frequencies(hist):
    """
    Calculates the log(f) and log(r) for each word in the histogram.

    Parameters:
        - hist (collections.Counter): A Counter object with word frequencies.

    Returns:
        - list: A list of tuples containing (word, log(f), log(r)) for each
        word.
    """

    log_frequencies = []
    rank = 1

    for word, count in hist.most_common():
        log_f = math.log(count)
        log_r = math.log(rank)
        log_frequencies.append((word, log_f, log_r))
        rank += 1

    return log_frequencies


def main():
    """
    Reads a text from a file, counts word frequencies, and
    prints one line for each word, in descending order of frequency,
    with log f and log r.
    """

    text = read_file(MARKOV)
    hist = count_word_frequencies(text)
    log_frequencies = calculate_log_frequencies(hist)
    print(os.path.basename(__file__))

    for word, log_f, log_r in log_frequencies:
        print(word, 'log(f)', log_f, 'log(r)', log_r)
