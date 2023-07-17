"""
This module contains a code for exercises 13-6 related to:
Think Python, 2nd Edition
Chapter 13: Case Study: Data Structure Selection


"""

def find_word_notin_list(file_book, file_words):
    with open(file_book,'r', encoding='utf-8') as book_file, open(file_words, 'r', encoding='utf-8') as words_file:
        book_file = set(book_file.read().lower().split())
        words_file = set(words_file.read().lower().split())

        words_notin_list = book_file - words_file
    
    print(words_notin_list)

file_book = 'D:/forGit/training_python/practice-2/texts/Ebook.txt'
file_words = 'D:/forGit/training_python/practice-2/texts/words.txt'

find_word_notin_list(file_book,file_words)
