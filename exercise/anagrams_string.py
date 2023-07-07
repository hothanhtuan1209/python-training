"""
Two words are anagrams if you can rearrange the letters
from one to spell the other. Takes two strings and returns 
True if they are anagrams.
"""
def is_anagram():
    # Enter two list a and b, then check them out
    a = list(input('Enter word a:'))
    b = list(input('Enter word b:'))
    
    if a == b[::-1]:
        return True
    else:
        return False

result = is_anagram()
print(result)
