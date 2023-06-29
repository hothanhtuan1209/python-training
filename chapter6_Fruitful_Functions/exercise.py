# Exercise 6-1.
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
x = 1
y = x + 1
print(c(x, y+3, x+y))

"""When the program starts running:
1. Initialize variable values x = 1 and y = 2 in the Global Frame.
2. Call the function c(x, y+3, x+y) and frame the function c. In the function framework c, x = 1, y = 5, and z = 3 (x =1, y = y + 3 = 2+3 = 5, z = x+y =1+2 =3)
3. Calculate the ‘total’ variable value by x + y + z, the result is 9 ( 1 + 5 + 3)
4. Call function b(total) and frame function b. In the function frame b, z = 9.
5. Call function a(x, y) with x = 9 + 1 = 10(a(z ,z)) returns x * y = 10 * 9 = 90
6. Assign the value of prod = a (z, z) = 90
7. finally returns the value b(total)**2 =90**2=8100 """

#Exercise 6-2.
def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))
result = ack(8, 9)
print(result)

#Exercise 6-3.
"""1. Type these functions into a file named palindrome.py and test them out. 
What happens if you call middle with a string with two letters? One letter? 
What about the empty string, which is written '' and contains no letters?"""
#In all 3 cases, middle function returns empty string because there is no value in between strings.

"""2. Write a function called is_palindrome that takes a string argument and returns
True if it is a palindrome and False otherwise. Remember that you can use the built-in 
function len to check the length of a string."""
def first(word):
    return word[0]
def last(word): 
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    else:
        return is_palindrome(middle(word))
result = is_palindrome('noon')
print(result) 

#Exercise 6-4.
"""A number, a, is a power of b if it is divisible by b and a/b is a power of b.
Write a function called is_power that takes parameters a and b and returns True 
if a is a power of b. Note: you will have to think about the base case."""
def checknumber(a,b):
    if a%b==0 and (a/b)%b ==0:
        return True
    else:
        return False
result = checknumber(9,3)
print(result)


#Exerecise 6-5:
"""The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.
One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b,
then gcd a, b = gcd b,r . As a base case, we can use gcd a, 0 = a."""

def gcd(a,b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)
result = gcd(8,12)
print(result)