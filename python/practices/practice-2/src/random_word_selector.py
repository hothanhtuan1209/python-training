"""
This module contains a code for exercises 13-7 related to:
Think Python, 2nd Edition
Chapter 13: Case Study: Data Structure Selection

Write a program that uses this algorithm to choose a random word from the book.
"""


import string
from random import randint
from bisect import bisect
import collections


def read_file(filename):
    """
    Reads a file and returns the processed word

    filename: string, name of the word list file

    return: counter object
    """

    hist = collections.Counter()
    fin = open(filename, 'r', encoding='utf8')

    for line in fin:
        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1

    return hist


def cumsum(list_word):
    """
    Calculates the cumulative sum of the elements in the list.

    list_word: list

    return: list
    """

    total = 0
    for i in range(len(list_word)):
        total += list_word[i]
        list_word[i] = total

    return list_word


def choose_random(hist):
    """
    Randomly generate a number and get the letter corresponding to that number

    hist: dict

    return: string
    """

    list_word = list(hist.keys())
    calculate_sum = cumsum(list(int(i) for i in hist.values()))
    total = calculate_sum[-1]
    random_val = randint(0, total - 1)
    index = bisect(calculate_sum, random_val)
    return list_word[index]


hist = read_file('ebook.txt')
print(choose_random(hist))
