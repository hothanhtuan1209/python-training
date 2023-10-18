def ack(m, n):
    """
    Calculate the Ackermann-Péter function for given non-negative integers.

    The Ackermann-Péter function is a recursive mathematical function defined
    for non-negative integer values 'm' and 'n'. It has the following rules:
    - If 'm' is 0, the result is 'n + 1'.
    - If 'm' is greater than 0 and 'n' is 0, the result is 'ack(m - 1, 1)'.
    - For other cases, the result is 'ack(m - 1, ack(m, n - 1))'.

    Parameters:
        - m (int): The non-negative integer 'm'.
        - n (int): The non-negative integer 'n'.

    Returns:
        int: The result of the Ackermann-Péter function for the given
        inputs 'm' and 'n'.
    """

    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))


result = ack(8, 9)
print(result)
