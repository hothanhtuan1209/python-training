"""Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace)."""
def print_words(file):
    fin = open(file)
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)
            
print_words('D:/forGit/training_python\chapter9_practice1/words.txt')
