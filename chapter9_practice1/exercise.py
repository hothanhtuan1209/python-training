# fin = open('D:/forGit/training_python\chapter9_practice1/words.txt')
# fin.readline()
# print(fin.readline())
# print(fin.readline())
# print(fin.readline())
# print(fin.readline())
# (fin.readline).closed()

# def print_long_words(filename):
#     with open(filename, 'r') as file:
#         words = file.read().split()
#         for word in words:
#             word_without_whitespace = word.replace(" ", "")
#             if len(word_without_whitespace) > 20:
#                 print(word)

# # Gọi hàm để in ra các từ có độ dài lớn hơn 20 ký tự
# print_long_words('D:/forGit/training_python\chapter9_practice1/words.txt')


def print_words(file):
    fin = open(file)
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

print_words('D:/forGit/training_python\chapter9_practice1/words.txt')