# """
# This module contains a code for exercises 13-5 related to:
# Think Python, 2nd Edition
# Chapter 13: Case Study: Data Structure Selection

# Write a function named choose_from_hist that takes a histogram as defined in 
# “Dictionary as a Collection of Counters” on page 127 and returns a random value from
# the histogram, chosen with probability in proportion to frequency.
# """

# import random

# def histogram(list_input):
#     """
#     Create 1 dictionary with letter as key and number of occurrences as value

#     list_input: list

#     return: dict
#     """
    
#     dict_hist = dict()
    
#     for letter in list_input:
#         if letter not in dict_hist:
#             dict_hist[letter] = 1
#         else:
#             dict_hist[letter] += 1
    
#     return dict_hist

# def choose_from_hist(dict_hist):
#     """
#     Generate 1 list of keys based on occurrences

#     dict_hist: dict
#     """
    
#     list_key = list()
#     for key, value in dict_hist.items():
#         for i in range(value):
#             list_key.append(key)
    
#     return random.choice(list_key)

# list_input = ['a', 'a', 'b', 'c', 'c', 'd', 'c']
# hist = histogram(list_input)

# print(choose_from_hist(hist))


import string
from random import randint
from bisect import bisect
import collections

def read_file(filename):
	'''adapted from author's answer
		Read a file and return histogram of frequency of every word
	'''
	hist  = collections.Counter()
	fp = open(filename, encoding="utf8")
	for line in fp:
		line = line.replace('-', ' ') # remove hyphens
		for word in line.split():
			word = word.strip(string.punctuation + string.whitespace) #remove punctuation and whitespace
			word = word.lower() #lowercase all the chars
			hist[word] = hist.get(word, 0) + 1 #increment if word is already encountered once else set to 1
	return hist
	
def cumsum(l):
	total = 0
	for i in range(len(l)):
		total += l[i]
		l[i] = total
	return l

def choose_from_random(hist):
	l = list(hist.keys()) # get word list
	#print(repr(l))
	cs = cumsum(list(int(i) for i in hist.values())) #cumulative sum of wordlist
	total = cs[-1] 
	x = randint(0,total-1)
	index = bisect(cs, x) #TODO: understand bisect
	return l[index]
	
if __name__ == '__main__':
	hist = read_file('D:/forGit/training_python/practice-2/texts/Ebook.txt')
	print(choose_from_random(hist))
	