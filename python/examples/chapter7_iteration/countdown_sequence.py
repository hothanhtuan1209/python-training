def countdown(n):
    """
    Print a countdown from 'n' to 1, and then print 'Blastoff!'

    Parameters:
        - n (int): The starting number for the countdown.
    """
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')


countdown(10)


def sequence(n):
    """
    Print a sequence starting from 'n' and following a specific pattern.

    The sequence starts with 'n' and continues until it reaches 1.
    If 'n' is even, it is divided by 2; if 'n' is odd, it is multiplied by 3
    and 1 is added. The sequence continues until 'n' becomes 1.

    Parameters:
        - n (int): The starting number for the sequence.
    """
    while n != 1:
        print(n)
        if n % 2 == 0:  # n is even
            n = n / 2
        else:  # n is odd
            n = n * 3 + 1


sequence(3)

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

while True:
    line = input('> ')
    if line == 'done':
        print(line)
        break
print('Done!')

while True:
    a = 4
    x = 3
    y = (x + a / x) / 2
    if y == x:
        break
    print(y)

print('a, mysqrt(a), math.sqrt(a), diff')
