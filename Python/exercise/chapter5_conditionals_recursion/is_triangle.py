"""
Write a function that prompts the user to input three stick lengths, converts
them to integers, and uses is_triangle to check whether sticks with the given
lengths can form a triangle.
"""


def is_triangle():
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    if (a > b + c) or (b > a + c) or (c > a + b):
        print('No')
    else:
        print('Yes')


is_triangle()
