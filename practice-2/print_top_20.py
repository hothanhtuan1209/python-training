"""
This module contains a code for exercises 13-3 related to:
Think Python, 2nd Edition
Chapter 13: Case Study: Data Structure Selection

Print the 20 most frequently used words in the book.

Dowload Ebook.txt file
"""

import string

def clean_word():
    """
    Read a file and count its word.

    returns: 
        - list words: list
        - count: int
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
            count += 1
    
    return cleaned_words

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

cleaned_words = clean_word()
word_counts = count_word_used(cleaned_words)

top_count = 20
for i, (word, count) in enumerate(word_counts.items()):
    print(i, word, count)
    if i+1 == top_count:
        break
