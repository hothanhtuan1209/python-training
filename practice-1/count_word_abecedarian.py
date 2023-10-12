"""
Write a function called is_abecedarian that returns True if the letters in a
word
appear in alphabetical order (double letters are okay). How many abecedarian
words are there?
"""


def is_abecedarian(word):
    """
    Check if a word is in alphabetical order.

    Parameters:
        word (str): The word to check for alphabetical order.

    Returns:
        bool: True if the word is in alphabetical order, False otherwise.
    """

    index = 0

    while index < len(word) - 1:
        if word[index] > word[index+1]:
            return False
        else:
            index += 1
    return True


list_word = input('Enter a list word:').split()
count = 0

for word in list_word:
    # Check and count the number of letters that satisfy the condition
    if is_abecedarian(word):
        count += 1

print('Abecedarian words:', count)
