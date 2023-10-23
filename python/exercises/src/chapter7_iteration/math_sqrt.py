import math


def mysqrt(a):
    """
    Calculate the square root of a number using the square root approximation
    method.

    Parameters:
        a (float): The number for which to calculate the square root.

    Returns:
        float: An approximation of the square root of 'a'.
    """

    x = a / 2
    while True:
        y = (x + a / x) / 2
        return y


def math_sqrt():
    """
    Compare the results of 'mysqrt' with the 'math.sqrt' function for numbers
    from 1 to 9.

    This function calculates the square root of numbers from 1 to 9 using both
    a custom approximation method 'mysqrt' and Python's 'math.sqrt' function.
    It prints a table comparing the results and the differences between them.
    """

    print('a     mysqrt(a)     math.sqrt(a)    diff')
    print('-     ----------   -------------    -----')
    a = 1
    while 1 <= a < 10:
        result_mysqrt = mysqrt(a)
        result_mathsqrt = math.sqrt(a)
        diff = abs(result_mysqrt - result_mathsqrt)
        print(a, '   ', result_mysqrt, '   ', result_mathsqrt, '   ', diff)
        a += 1
