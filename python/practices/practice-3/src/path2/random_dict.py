"""
Write a function named choose_from_hist that takes a histogramand returns
a random value from the histogram, chosen with probability in proportion
to frequency.
"""


import random
import os
from helpers.user_input import get_user_input


def histogram(input_string):
    """
    Create a dictionary with letters as keys and their frequencies as values.

    Parameters:
        - input_string (str): A string of input letters.

    Returns:
        - dict: A dictionary containing letters as keys and their frequencies
        as values.
    """

    dict_hist = {}

    for letter in input_string:
        if letter not in dict_hist:
            dict_hist[letter] = 1
        else:
            dict_hist[letter] += 1

    return dict_hist


def choose_from_hist(dict_hist):
    """
    Choose a random value from the histogram based on the frequency of
    occurrences.

    Parameters:
        - dict_hist (dict): A dictionary representing a histogram with items
        and their frequencies.

    Returns:
        - str: A randomly chosen item from the histogram, selected with
        probability proportional to its frequency.
    """

    list_key = []

    for key, value in dict_hist.items():
        for i in range(value):
            list_key.append(key)

    return random.choice(list_key)


def main():
    """
    Allows the user to input a string of letters and calculates the
    frequency of each letter, allowing the user to choose a random letter
    with probability in proportion to its frequency.
    """

    print(os.path.basename(__file__))
    user_input = get_user_input("Enter a string of letters: ")

    dict_histogram = histogram(user_input)
    print(choose_from_hist(dict_histogram))
