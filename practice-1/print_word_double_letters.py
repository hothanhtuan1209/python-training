def is_triple_double(word):
    # Find three consecutive double letters
    i = 0
    count = 0
    while i < len(word)-1:
        # Check through 2 characters next to each other
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i +=2
        else:
            i = i + 1 - 2*count
            count = 0
    return False

def find_triple_double():
    # Reads a word list and prints words with triple double letters.
    fin = open('D:/forGit/training_python\practice-1/words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)

print('three consecutive double letters is: ')
find_triple_double()
