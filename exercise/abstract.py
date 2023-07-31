"""
Create class Shape to apply abstract
"""

import math

class Shape:
    def calculator_area(self):
        pass

    def calculator_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculator_area(self):
        return math.pi * self.radius**2

    def calculator_perimeter(self):
        return math.pi * 2 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculator_area(self):
        return self.length * self.width
    
    def calculator_perimeter(self):
        return (self.length + self.width) * 2

circle = Circle(5)
print(circle.calculator_area())

rectangle = Rectangle(3, 5)
print(rectangle.calculator_perimeter())
