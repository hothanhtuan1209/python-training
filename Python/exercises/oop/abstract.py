"""
Create class Shape to apply abstract
"""


import math


class Shape:
    """
    Represents a generic shape.

    Methods:
        calculator_area(self): Abstract method to calculate the area of the
        shape.
        calculator_perimeter(self): Abstract method to calculate the perimeter
        of the shape.
    """

    def calculator_area(self):
        """
        Abstract method to calculate the area of the shape.
        This method must be implemented in subclasses.
        """

        pass

    def calculator_perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        This method must be implemented in subclasses.
        """

        pass


class Circle(Shape):
    """
    Represents a circle, a type of shape.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        __init__(self, radius): Initializes a Circle object with the given
        radius.
        calculator_area(self): Calculates the area of the circle.
        calculator_perimeter(self): Calculates the perimeter of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle object with the given radius.

        Parameters:
            radius (float): The radius of the circle.
        """

        self.radius = radius

    def calculator_area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """

        return math.pi * self.radius**2

    def calculator_perimeter(self):
        """
        Calculates the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """

        return math.pi * 2 * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle, a type of shape.

    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Methods:
        __init__(self, length, width): Initializes a Rectangle object with the
        given length and width.
        calculator_area(self): Calculates the area of the rectangle.
        calculator_perimeter(self): Calculates the perimeter of the rectangle.
    """

    def __init__(self, length, width):
        """
        Initializes a Rectangle object with the given length and width.

        Parameters:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """

        self.length = length
        self.width = width

    def calculator_area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """

        return self.length * self.width

    def calculator_perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """

        return (self.length + self.width) * 2


circle = Circle(5)
print("Circle area:", circle.calculator_area())

rectangle = Rectangle(3, 5)
print("Rectangle perimeter:", rectangle.calculator_perimeter())
