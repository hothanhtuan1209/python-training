"""
Takes a list and returns a new list that contains all
but the first and last elements.
"""
t = [1, 2, 3, 4, 5, 6, 7]
def middle(t):
    # Take elements have index 1 to index len(1)-1
    b = t[1:(len(t)-1)]
    print(b)

middle(t)
