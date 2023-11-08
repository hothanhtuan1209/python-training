"""
Check the list of words to see if for each word the letters inside are in
alphabetical order
"""


import os


def check_alphabetical_order(word):
    """
    Check if a word is in alphabetical order.

    Parameters:
        word (str): The word to check for alphabetical order.

    Returns:
        bool: True if the word is in alphabetical order, False otherwise.
    """

    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False

    return True


def count_abecedarian_words(word_list):
    """
    Count the number of words in a list that have letters in alphabetical
    order.

    Parameters:
        word_list (list of str): A list of words.

    Returns:
        int: The count of abecedarian words.
    """

    count = 0
    for word in word_list:
        if check_alphabetical_order(word):
            count += 1
    return count


def main():
    """
    Prints the words in the list with the letters in the words arranged
    in alphabetical order
    """

    print(os.path.basename(__file__))
    input_text = input('Enter a list of words: ')
    list_word = input_text.split()
    count = count_abecedarian_words(list_word)

    print('Abecedarian words:', count)
