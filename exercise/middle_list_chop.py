"""
Takes a list, modifies it by removing the first and last
elements, and returns None.
"""
t = [1, 2, 3, 4, 5]
def chop(t):
    # Function remove the first and last element 
    del t[:1]
    del t[-1:]
    print(t)

chop(t)
