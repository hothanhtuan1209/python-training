#function calls
type(42)
int(3.9)

#Math functions
import math
ratio = signal_power / noise_power
decibels = 10*math.log10(ratio)

radians = 0.7
height = math.sin(radians)

#add new function
def print_myconpanyname():
    print('Agility')

type(print_myconpanyname)

print_myconpanyname()


def company():
    print_myconpanyname()
company()

#Parametter and arguments
def test(hello):
    print()
    print()
test('World')
test('World'*4)

def cat_twice(part1, part2):
    cat = part1 + part2
    print(cat)
cat_twice(2,3)


