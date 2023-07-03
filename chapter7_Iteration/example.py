def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

countdown(10)

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0: # n is even
            n = n / 2
        else: # n is odd
            n = n*3 + 1
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
    a=4
    x=3
    y = (x + a/x) / 2
    if y == x:
        break
    print(y)
    break
print('a, mysqrt(a), math.sqrt(a), diff')
