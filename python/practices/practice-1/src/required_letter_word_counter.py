"""
1. Write a function named uses_all that takes a word and a string of required
letters, and that returns True if the word uses all the required letters
at least once.
2. How many words are there that use all the vowels aeiou? How about aeiouy?
"""


def uses_all(word, required_letters):
    """
    Check if a word contains all the required letters.

    Parameters:
        - word (str): The word to check.
        - required_letters (str): A string containing the letters that must be
        present in 'word'.

    Returns:
        - bool: True if 'word' contains all the required letters, False
        otherwise.
    """

    for letter in required_letters:
        if letter not in word:
            return False

    return True


def count_words_vowel(required_letters):
    """
    Count the number of words in a list that contain all the required letters.

    Parameters:
        - required_letters (str): A string containing the letters that must be
        present in each word.

    Returns:
        - int: The count of words that contain all the required letters.
    """

    words = input("Enter a list of words: ").split()
    count = 0

    for word in words:
        if uses_all(word, required_letters):
            count += 1

    return count


print(count_words_vowel("aeiou"))
