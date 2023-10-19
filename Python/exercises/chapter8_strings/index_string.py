def print_letter(word):
    """
    Return characters with even indices from the input word.

    Parameters:
        - word (str): The input word.

    Returns:
        - str: The characters with even indices from the word.
    """

    return word[0:9:2]


result = print_letter('responsibility')
print(result)
