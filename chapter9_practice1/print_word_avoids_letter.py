"""Write a function named avoids that takes a word and a string of forbidden letters,
# and that returns True if the word doesn’t use any of the forbidden letters."""
def avoids_letter():
    words = 'hello@'
    forbidden_letter = '!@#$%*&'
    for letter in forbidden_letter:
        if letter in words:
            return False
    return True
results = avoids_letter()
print(results)  

# """Modify your program to prompt the user to enter a string of forbidden letters and
# then print the number of words that don’t contain any of them. Can you find a combination of five forbidden letters that excludes the smallest number of words?"""
# def avoids_letter():
#     words = input('Enter words separated by space:').split()
#     letters = input('Enter a string of forbidden letters:')
#     total = 0
#     for word in words:
#         if any(letter in word for letter in letters):
#             continue
#         total += 1
#     print(total)
# avoids_letter()
