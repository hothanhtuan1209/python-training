def any_lowercase1(s):
    """
    Check if a string `s` contains any lowercase characters.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if the string contains lowercase characters, False if not.
    """
    for c in s:
        if c.isupper():
            return False
    return True


result1 = any_lowercase1('banaNa')
print(result1)


def any_lowercase2(s):
    """
    Check if a string `s` contains any lowercase characters.

    Parameters:
        s (str): The string to check.

    Returns:
        str: 'True' if the string contains lowercase characters, 'False'
        if not.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


result2 = any_lowercase2('banaNa')
print(result2)


def any_lowercase3(s):
    """
    Check if a string `s` contains any lowercase characters.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if the string contains lowercase characters, False if not.
    """
    for c in s:
        flag = c.islower()
    return flag


result3 = any_lowercase3('banaNa')
print(result3)


def any_lowercase4(s):
    """
    Check if a string `s` contains any lowercase characters.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if the string contains lowercase characters, False if not.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


result4 = any_lowercase4('banaNa')
print(result4)


def any_lowercase5(s):
    """
    Check if a string `s` contains any lowercase characters.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if the string contains lowercase characters, False if not.
    """
    for c in s:
        if not c.islower():
            return False
    return True


result5 = any_lowercase5('banaNa')
print(result5)
