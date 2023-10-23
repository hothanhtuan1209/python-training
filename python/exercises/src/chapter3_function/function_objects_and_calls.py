"""
This code defines functions to demonstrate function objects and function calls.

1. do_twice(f, values) - This function takes a function object 'f' and a value
'values' as arguments and calls 'f' twice, passing 'values' as an argument.
It uses the function object 'f' to perform an action on the value.

2. print_twice(values) - This function takes a value 'values' and prints it
twice, simulating the behavior of 'print' function called twice.

3. do_four(f, values) - This function takes a function object 'f' and a value
'values' as arguments and calls 'f' four times, passing 'values' as a
parameter. It utilizes the 'do_twice' function to perform the action four
times with 'values'.

The code then demonstrates the use of these functions by calling 'do_twice' to
print 'spam' twice, and 'do_four' to print 'spam' four times.

File Name: function_objects_and_calls.py
"""


def do_twice(f, values):
    """
    Call the given function object 'f' twice, passing the 'values' as an
    argument.

    Parameters:
        - f (function): The function object to be called.
        - values (any): The value to be passed as an argument to 'f'.

    This function takes a function object 'f' and a value 'values' as
    arguments and calls 'f' twice, passing 'values' as an argument to 'f'.
    """

    f(values)
    f(values)


def print_twice(values):
    """
    Print the given value twice.

    Parameters:
    values (any): The value to be printed.

    This function takes a value 'values' and prints it twice.
    """

    print(values)
    print(values)


def do_four(f, values):
    """
    Call the given function object 'f' four times, passing the 'values' as a
    parameter.

    Parameters:
        - f (function): The function object to be called.
        - values (any): The value to be passed as a parameter to 'f'.

    This function takes a function object 'f' and a value 'values' as
    arguments and calls 'f' four times, passing 'values' as a parameter to 'f'.
    """

    do_twice(f, values)
    do_twice(f, values)


do_twice(print_twice, 'spam')
do_four(print, 'spam')
