#exercise 8-2
def count_a():
    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)
count_a()


#exercise 8-3
def print_letter(word):
    return word[0:9:2]
result=print_letter('responsibility')
print(result)



#exercise 8-4

def any_lowercase1(s):
    for c in s:
        if c.isupper():
            return False
    return True
result=any_lowercase1('banaNa')
print(result)

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# →This function is quite wrong because 'c' is a string, not a representation of the variable in the string s

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# →This function only checks the first character and returns the flag variable, the rest of the characters in the string are not checked.

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# →This function is wrong because it only needs to appear 1 lowercase character, the function returns True

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
result=any_lowercase5('banAna')
print(result)
# →This is the correct function
#exercise 8-5

