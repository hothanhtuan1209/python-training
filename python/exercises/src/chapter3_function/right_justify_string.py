"""
Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the
string is in column 70 of the display
"""


def right_justify(s):
    """
    Right-justify a string within a 70-character wide field and print
    the result.

    Parameters:
     - s (str): The string to be right-justified.
    """

    spaces = " " * (70 - len(s))
    right_justified = spaces + s
    print(right_justified)


right_justify('Agility')
