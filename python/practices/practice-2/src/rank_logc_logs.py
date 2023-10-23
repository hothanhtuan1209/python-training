"""
This module contains a code for exercises 13-9 related to:
Think Python, 2nd Edition
Chapter 13: Case Study: Data Structure Selection

Write a program that reads a text from a file, counts word frequencies, and
prints one line for each word, in descending order of frequency, with log f
and log r.
"""


import string
import math
import collections


def read_file(filename):
    """
    Reads a text from a file and returns it as a string.

    filename: string, name of the test file

    returns: string
    """

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def count_word_frequencies(text):
    """
    Counts the frequencies of words in the given text.

    text: string

    returns: Counter object
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

    hist: Counter object

    returns: list of tuples (word, log(f), log(r))
    """

    log_frequencies = []
    total_words = sum(hist.values())
    rank = 1

    for word, count in hist.most_common():
        log_f = math.log(count)
        log_r = math.log(rank)
        log_frequencies.append((word, log_f, log_r))
        rank += 1

    return log_frequencies


filename = "markov.txt"
text = read_file(filename)
hist = count_word_frequencies(text)
log_frequencies = calculate_log_frequencies(hist)

for word, log_f, log_r in log_frequencies:
    print(word, "log(f)", log_f, "log(r)", log_r)
