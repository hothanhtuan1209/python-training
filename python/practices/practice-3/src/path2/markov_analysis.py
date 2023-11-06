"""
Write a program to read a text from a file and perform Markov analysis. The
result should be a dictionary that maps from prefixes to a collection of
possible suffixes.
"""


import random
import os
from helpers.file_reader import read_file_content
from helpers.user_input import get_user_input
from constant.constant_file import path_of_markov_file


def perform_markov_analysis(text, prefix_length):
    """
    Perform Markov analysis on the given text.

    Parameters:
        text (str): The input text to be analyzed.
        prefix_length (int): The length of the prefix for Markov analysis.

    Returns:
        dict: A dictionary mapping from prefixes to a collection of possible
        suffixes.
    """

    prefixes = {}
    words = text.split()

    for i in range(len(words) - prefix_length):
        prefix = tuple(words[i: i + prefix_length])
        suffix = words[i + prefix_length]

        if prefix in prefixes:
            prefixes[prefix].append(suffix)
        else:
            prefixes[prefix] = [suffix]

    return prefixes


def generate_random_text(prefixes, prefix_length, num_words):
    """
    Generate random text using the Markov analysis results.

    Parameters:
        prefixes (dict): Markov analysis results represented as a dictionary.
        prefix_length (int): The length of the prefix for Markov analysis.
        num_words (int): The number of words in the generated text.

    Returns:
        str: A randomly generated text.
    """

    random_text = ''
    prefix_list = list(random.choice(list(prefixes.keys())))

    for _ in range(num_words):
        prefix = tuple(prefix_list[-prefix_length:])

        if prefix in prefixes:
            suffix = random.choice(prefixes[prefix])
            random_text += suffix + ' '
            prefix_list.append(suffix)
        else:
            break

    return random_text.strip()


def main():
    """
    Main function of the program.
    """

    print(os.path.basename(__file__))
    file_content = read_file_content(path_of_markov_file)

    if file_content is not None:
        number_of_words = int(get_user_input('Enter number of words:'))
        prefix_length = int(get_user_input("Enter prefix length:"))

        prefixes = perform_markov_analysis(file_content, prefix_length)
        random_text = generate_random_text(
            prefixes,
            prefix_length,
            number_of_words
        )

        print(random_text)
