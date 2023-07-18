"""
This module contains a code for exercises 13-4 related to:
Think Python, 2nd Edition
Chapter 13: Case Study: Data Structure Selection

Print all the words in the book that are not in the word list.

Dowload file word.txt and file Ebook.txt
"""

def read_word_list(filename):
    """
    Reads a word list file and returns a list of words.

    filename: string, name of the word list file
    
    returns: list
    """
    
    word_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        
        for line in file:
            word = line.strip()
            word_list.append(word)
    
    return word_list

def find_missing_words(book_filename, words_filename):
    """
    Finds all words in book file that do not appear in words file.

    book_filename: string, name of the test file
    words_filename: string, name of the words file
    
    returns: list of missing words
    """
    
    test_words = read_word_list(book_filename)
    words_list = read_word_list(words_filename)
    missing_words = []
    
    for word in test_words:
        if word not in words_list:
            missing_words.append(word)
    
    return missing_words

book_file = 'Ebook.txt'
words_file = 'words.txt'

missing_words = find_missing_words(book_file, words_file)
for word in missing_words:
    print(word)
