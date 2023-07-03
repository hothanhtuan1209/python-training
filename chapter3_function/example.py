# Math functions
import math

signal_power = 4
noise_power = 5
ratio = signal_power / noise_power
decibels = 10*math.log10(ratio)
radians = 0.7
height = math.sin(radians)

# Add new function
def print_myconpanyname():
    print('Agility')
print_myconpanyname()

def company():
    print_myconpanyname()
company()

# Parametter and arguments
def test(hello):
    print()
    print()
test('World')
test('World'*4)

def cat_twice(part1, part2):
    cat = part1 + part2
    print(cat)
cat_twice(2,3)
