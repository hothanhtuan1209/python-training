#Exercise9-1:
"""Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace)."""
def print_words(file):
    fin = open(file)
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)
print_words('D:/forGit/training_python\chapter9_practice1/words.txt')

# Exercise 9-2:
"""Write a function called has_no_e that returns True if the given word doesn’t have the
letter “e” in it."""
def has_no_e():
    word = input('Enter a word or string:')
    for letter in word:
        if letter == 'e' or letter == 'E':
            return False
        else:
            return True
result = has_no_e()
print(result)

"""Modify your program from the previous section to print only the words that have no
“e” and compute the percentage of the words in the list that have no “e”."""
