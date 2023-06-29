
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

fruit = 'banana'
index = -1
while True:
    if abs(index) < len(fruit):
        letter = fruit[index]
        print(letter)
        index -=1
    elif abs(index) == len(fruit):
        letter = fruit[0]
        print(letter)
        break

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == ('O') or letter == ('Q'):
        print(letter +'u'+suffix)
    else:   
        print(letter + suffix)

s = 'Monty Python'
a = s[2:2]
print(a)