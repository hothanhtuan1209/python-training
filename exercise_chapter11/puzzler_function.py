"""
This module contains a code for exercises 11-6 related to:
Think Python, 2nd Edition
Chapter 11: Dictionaries

This exercise requires finding words in the word.txt file
if the word has 5 letters and if the first letter is kept or removed,
the pronunciation is still the same. The pronunciation is taken from
the file c06d.txt

Download file c06d.txt and words.txt
"""

def read_pronounce():
    """
    Create a dictionaries of keys with length 5 and the value is
    the pronunciation in the file c06d.txt

    return: dict 
    """
    
    pronounce = {}
    fin = open('c06d.txt')
    
    for line in fin:
        line = line.strip().split(" ")

        if len(line[0]) == 5:            
            key = line[0]
            value = " ".join(line[1:]) 
            pronounce[key] = value

    fin.close()
    
    return pronounce

pronounce = read_pronounce()

def read_words():
    """
    Create a list containing words of length 5

    return: list of words
    """
    
    list_word = []
    fin = open('words.txt')
    
    for line in fin:
        line = line.strip()
        
        if len(line) == 5:
            list_word = list_word + [line]
    
    fin.close()
    
    return list_word

list_word = read_words()

def get_homophones(list_word, pronounce):
    """
    Returns words with the same pronunciation

    pronounce: dict
    list_word: list

    return: list
    """
    
    result = []

    for word in list_word:
        word_pronounce = pronounce.get(word, "")

        if word_pronounce:
            if pronounce.get(word[1:], "") == word_pronounce:
                result.append(word)

    return result

homophone_words = get_homophones(list_word, pronounce)
print(homophone_words)
