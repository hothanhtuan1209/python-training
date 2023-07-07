"""
Takes a list as a parameter and returns True if
the list is sorted in ascending order and False otherwise.
"""
t = [1, 2, 3, 4, 5]
def is_sorted(t):
    # Check ascending order
    index = 0
    
    while index < len(t)-1:
        # Iterate over each element in the list 't'
        if t[index] > t[index+1]:
            return False
        else:
            index +=1

    return True

print(is_sorted(t))
