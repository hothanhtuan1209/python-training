"""
This module contains a code for exercises 12-4 related to:
Think Python, 2nd Edition
Chapter 12: Tuples

Sprite --> spite --> spit --> pit --> it --> i
Write a program to find all words that can be reduced in this way 
and then find the longest one.
"""

def make_word_dict():
    """
    Reads a word list and returns a dictionary.

    returns: dict
    """
    
    dict_words = dict()
    fin = open('D:/forGit/training_python/practice-1/words.txt')
    for line in fin:
        word = line.strip().lower()
        dict_words[word] = None

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        dict_words[letter] = letter
    return dict_words

"""
memo is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children.  It starts
with the empty string.
"""

memo = {}
memo[''] = ['']

def is_reducible(word, word_dict):
    """
    If word is reducible, returns a list of its reducible children.

    Also adds an entry to the memo dictionary.

    A string is reducible if it has at least one child that is 
    reducible.  The empty string is also reducible.

    word: string
    word_dict: dictionary with words as keys
    """
    
     # if have already checked this word, return the answer
    if word in memo:
        return memo[word]

    # check each of the children and make a list of the reducible ones
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)

    # memoize and return the result
    memo[word] = res
    return res

def children(word, word_dict):
    """
    Returns a list of all words that can be formed by removing one letter.

    word: string

    returns: list of strings
    """
    
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res

def all_reducible(word_dict):
    """
    Checks all words in the word_dict; returns a list reducible ones.

    word_dict: dictionary with words as keys
    """
    
    res = []
    for word in word_dict:
        word_reduced = is_reducible(word, word_dict)
        if word_reduced != []:
            res.append(word)
    return res

def print_trail(word):
    """
    Prints the sequence of words that reduces this word to the empty string.

    If there is more than one choice, it chooses the first.

    word: string
    """
    
    if len(word) == 0:
        return
    print(word, end=' ')
    word_reduced = is_reducible(word, word_dict)
    print_trail(word_reduced[0])

def print_longest_words(word_dict):
    """
    Finds the longest reducible words and prints them.

    word_dict: dictionary of valid words
    """
    
    words = all_reducible(word_dict)
    word_reduced = []
    
    for word in words:
        word_reduced.append((len(word), word))
    word_reduced.sort(reverse=True)

    for _, word in word_reduced[0:5]:
        print_trail(word)
        print('\n')

word_dict = make_word_dict()
print_longest_words(word_dict)
