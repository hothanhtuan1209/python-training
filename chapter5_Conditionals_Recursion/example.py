#Alternative Execution
x=10
y=15
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

#Chained Conditionals
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

#Nested Conditionals
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')


#Recursion
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


#Keyboard Input
text = input()
print(text)
