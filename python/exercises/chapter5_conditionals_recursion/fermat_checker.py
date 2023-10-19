"""
Write a function that prompts the user to input values for a, b, c and n,
converts them to integers, and uses check_fermat to check whether they violate
Fermat's theorem"""


def check_fermat(a, b, c, n):
    """
    Check if Fermat's Last Theorem holds for the given values.

    Parameters:
        - a (int): The first integer value.
        - b (int): The second integer value.
        - c (int): The third integer value.
        - n (int): The exponent value.
    """

    if n > 2 and (a**n + b**n == c**n):
        print('Holy smokes, Fermat was wrong')
    else:
        print("no, that doesn't work")


def input_check_fermat():
    """
    Prompt the user to input values and check Fermat's Last Theorem.

    This function prompts the user to input values for 'a', 'b', 'c', and 'n'
    and then calls the 'check_fermat' function to check whether Fermat's Last
    Theorem holds for the provided values.
    """

    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    n = int(input('n='))
    check_fermat(a, b, c, n)


input_check_fermat()
