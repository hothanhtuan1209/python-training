"""Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once."""
def uses_all(word, required_letters):
    for letter in required_letters:
        if letter not in word:
            return False
    return True
# print(uses_all())

""" How many words are there that use all the vowels aeiou? How about aeiouy?"""

def count_words_vowel(required_letters):
    words = input('Enter a list of words: ').split()
    count = 0
    for word in words:
        if uses_all(word, required_letters):
            count += 1
    return count
print(count_words_vowel('aeiou'))