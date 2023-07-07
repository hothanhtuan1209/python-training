"""
Takes a list and returns True if there is
any element that appears more than once.
"""
def has_duplicates():
    t = list(input('Enter list:'))
    b = set(t)
    # Use set() to remove matching characters in list 't' then assign to 'b'
    
    if len(t) == len(b):
        return False
    return True

print(has_duplicates())
