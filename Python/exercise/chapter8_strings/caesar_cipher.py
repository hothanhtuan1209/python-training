def caesar_cipher(word, n):
    """
    Perform Caesar cipher encryption on the input word.

    Parameters:
        word (str): The input word to be encrypted.
        n (int): The number of positions to shift each character.

    Returns:
        str: The Caesar cipher encrypted word.
    """

    result = ""
    for letter in word:
        if letter.isalpha():
            if letter.isupper():
                result += chr((ord(letter) - 65 + n) % 26 + 65)
            else:
                result += chr((ord(letter) - 97 + n) % 26 + 97)
        else:
            result += letter
    return result


cipher_word = caesar_cipher("Agility.io", 3)
print(cipher_word)
