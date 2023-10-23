"""
1. Write a function named avoids that takes a word and a string of forbidden
letters, and that returns True if the word doesn't use any of the forbidden
letters.
2. Modify your program to prompt the user to enter a string of forbidden
letters and then print the number of words that don't contain any of them.
Can you find a combination of five forbidden letters that excludes the
smallest number of words?

def avoids():
    words = 'hello@'
    forbidden_letter = '!@#$%*&'
    for letter in forbidden_letter:
        if letter in words:
            return False
    return True
results = avoids()
print(results)
"""


def avoids():
    """
    Count the total number of words that do not contain any of the forbidden
    letters.
    """

    words = input('Enter words separated by space:').split()
    letters = input('Enter a string of forbidden letters:')

    for total, word in enumerate(words):
        # Does each word in word contain each letter in letters?
        if any(letter in word for letter in letters):
            continue

    print(total)


avoids()
