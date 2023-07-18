"""
This module contains a code for exercises 13-2 related to:
Think Python, 2nd Edition
Chapter 13: Case Study: Data Structure Selection

Modify the program to count the total number of words in the book, and the
number of times each word is used. Print the number of different words used in the book.

Download Ebook.txt file
"""

import string

def clean_word():
    """
    Read a file and count its word.

    returns: list words: list and count: int
    """

    fin = open('Ebook.txt',encoding='utf-8')
    cleaned_words = []
    count = 0

    for line in fin:
        line = line.strip().split()

        for word in line:
            cleaned_word = ""
            
            for letter in word:
                if letter not in string.whitespace and letter not in string.punctuation:
                    cleaned_word += letter.lower()
            
            cleaned_words.append(cleaned_word)
            count +=1
    
    return cleaned_words, count

def count_word_diff(cleaned_words):
    """
    Count the number of different words used

    cleaned_words: list

    return: word_in_book: list and word_diff: int
    """
    
    word_in_book = []
    word_diff = 0
    
    for word in cleaned_words:
        if word not in word_in_book:
            word_in_book.append(word)
            word_diff +=1
    
    return word_in_book,word_diff

def count_word_used(cleaned_words):
    """
    Count the number of times each word is used and sorted

    cleaned_words: list

    return: dict
    """
    
    count_each_word = {}

    for word in cleaned_words:
        if word in count_each_word : 
            count_each_word[word] +=1
        else:
            count_each_word[word] = 1
    
    sorted_count_each_word = dict(sorted(count_each_word.items(), key=lambda x: x[1], reverse=True)) 
    
    return sorted_count_each_word

cleaned_words, count = clean_word()
word_in_book=count_word_diff(cleaned_words,count)
print(count_word_used(cleaned_words))
