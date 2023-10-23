# Filename: function_tests.py

def test(hello):
    """
    Print two empty lines, followed by the input parameter 'hello'.

    Parameters:
    -   - hello (str): The string to be printed after two empty lines.
    """
    print()
    print()
    print(hello)


test('World')
test('World' * 4)


def cat_twice(part1, part2):
    """
    Concatenate two values 'part1' and 'part2', then print the result.

    Parameters:
        - part1: The first part to be concatenated.
        - part2: The second part to be concatenated.
    """
    cat = part1 + part2
    print(cat)


cat_twice(2, 3)
