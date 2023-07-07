"""
This exercise requires entering a list and printing a 
new list with the i + n = i + (i + 1) + (i+2) +...+ (i+n-1)
"""
numbers_a = [5, 7, 9]

def cumsum(numbers_a):
    # This function calculate list 'number_b' based on list 'number_a'
    sum = 0
    numbers_b = []
    
    for number in numbers_a:
        sum += number
        numbers_b.append(sum)
    
    return numbers_b

print(cumsum(numbers_a))
