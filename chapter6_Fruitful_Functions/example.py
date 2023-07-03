# Return Values
import math

def area(radius):
    a = math.pi * radius**2
    return a

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
    
# Incremental Development
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

# Boolean Functions
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
is_divisible(6,4) # False 

# More Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
    return result
factorial(5)

# One More Example
def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    