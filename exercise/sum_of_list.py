"""
The exercise asks you to calculate the sum of
all the elements in the list
"""
t = [[1, 2], [3], [4, 5, 6]]
def nested_sum(t):
    # Function nested_sum print sum of list 't'
    total = 0 
    
    for i in (t):
        total += sum(i)
    print(total)

nested_sum(t)
