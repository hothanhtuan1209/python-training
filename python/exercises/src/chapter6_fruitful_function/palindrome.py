"""
Write a function called is_palindrome that takes a string argument and returns
True if it is a palindrome and False otherwise. Remember that you can use the
built-in function len to check the length of a string.
"""


def first(word):
    """
    Get the first character of a word.

    Parameters:
        word (str): The word from which to extract the first character.

    Returns:
        str: The first character of the word.
    """

    return word[0]


def last(word):
    """
    Get the last character of a word.

    Parameters:
        word (str): The word from which to extract the last character.

    Returns:
        str: The last character of the word.
    """

    return word[-1]


def middle(word):
    """
    Get the middle characters of a word, excluding the first and last
    characters.

    Parameters:
        word (str): The word from which to extract the middle characters.

    Returns:
        str: The middle characters of the word.
    """

    return word[1:-1]


def is_palindrome(word):
    """
    Check if a word is a palindrome (reads the same forwards and backwards).

    Parameters:
        word (str): The word to check for palindrome property.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """

    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    else:
        return is_palindrome(middle(word))


result = is_palindrome('noon')
print(result)
