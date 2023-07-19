"""
This module contains a code for exercises 13-6 related to:
Think Python, 2nd Edition
Chapter 13: Case Study: Data Structure Selection

Write a program that uses set subtraction to find words in the book
that are not in the word list.

Dowload file word.txt and file ebook.txt
"""

def find_word_notin_list(file_book, file_words):
    """
    Find word in book but not in words list

    file_book: string, name of the test file
    file_words: string, name of the test file

    print set words
    """
    
    with open(file_book,'r', encoding = 'utf-8') as book_file, open(file_words, 'r', encoding = 'utf-8') as words_file:
        book_file = set(book_file.read().lower().split())
        words_file = set(words_file.read().lower().split())

        words_notin_list = book_file - words_file
    
    print(words_notin_list)

file_book = 'ebook.txt'
file_words = 'words.txt'

find_word_notin_list(file_book,file_words)
