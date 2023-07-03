"""Write a function called has_no_e that returns True if the given word doesn’t have the
letter “e” in it."""
def has_no_e():
    word = input('Enter a word or string:')
    for letter in word:
        if letter == 'e' or letter == 'E':
            return False
    return True
result = has_no_e()
print(result)

"""Modify your program from the previous section to print only the words that have no
“e” and compute the percentage of the words in the list that have no “e”."""
def count_words():
    words = input("Enter the list of words: ").split()
    count_word = len(words)
    words_has_no_e = 0
    for word in words:
        if 'e' not in word and 'E' not in word:
            print(word)
            words_has_no_e +=1
    percentage = (words_has_no_e/count_word) * 100
    print('Percentage of words without the letter e',percentage)
count_words()
