minutes = 105
minutes / 60
hours = minutes//60

remainder = minutes-hours*60

remainder = minutes % 60

#Boolean Expressions
5==5 # True
5==6 # False
x=1
y=2
x != y # x is not equal to y
x > y # x is greater than y
x < y # x is less than y
x >= y # x is greater than or equal to y
x <= y # x is less than or equal to y

#Alternative Execution
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
