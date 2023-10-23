"""
Write a function named uses_only that takes a word and a string of letters,
and that returns True if the word contains only letters in the list
"""


def used_only(word, string_letter):
    """
    Check if a word contains only the specified letters.

    Parameters:
        - word (str): The word to check.
        - string_letter (str): A string containing the allowed letters.

    Returns:
        - bool: True if 'word' contains only letters from 'string_letter',
        False otherwise.
    """
    for letter in word:
        if letter not in string_letter:
            return False

    return True


print(used_only('hello', 'leo'))
