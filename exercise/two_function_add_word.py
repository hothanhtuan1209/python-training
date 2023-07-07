"""
Reads the file words.txt and builds a list with one element per
word. Write two versions of this function, one using the append
method and the other using the idiom t = t + [x].
"""
def word_list_append():
    word_list = []
    read_file = open('D:/forGit/training_python\practice-1/words.txt')
    # This function adds words to word_list using 'append'

    for line in read_file:
        word = line.strip()
        word_list.append(word)
    
    return word_list

word_list_append()

def word_list_concatenate():
    word_list = []
    read_file = open('D:/forGit/training_python\practice-1/words.txt')
    # This function adds words to word_list using the idiom t = t + [x]

    for line in read_file:
        word = line.strip()
        word_list = word_list + [word]
    
    return word_list

word_list_concatenate()
