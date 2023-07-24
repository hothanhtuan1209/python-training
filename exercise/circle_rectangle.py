"""
This module contains a code for exercises 15-1 related to:
Think Python, 2nd Edition
Chapter 15: Classes and Objects

- Write a definition for a class named Circle with attributes center and radius
- Write a function named point_in_circle that takes a Circle and a Point
- Write a function named rect_in_circle that takes a Circle and a Rectangle
- Write a function named rect_circle_overlap that takes a Circle and a Rectangle
"""

import math

class Circle:
    """
    Represents a circle with attributes center and radius.
    """

    def __init__(self, center, radius):
        """
        Initializes a Circle object.

        center (Point): The center of the circle.
        radius (float): The radius of the circle.
        """
        
        self.center = center
        self.radius = radius

class Point:
    """
    Represents a point with attributes x and y.
    """
    
    def __init__(self, x, y):
        """
        Initializes a Point object.

        x (float): represent coordinates in 2D space
        y (float): represent coordinates in 2D space 
        """
        
        self.x = x
        self.y = y

def distance(point_1, point_2):
    """
    Calculate distance between 2 points in 2D space.

    point_1: Coordinates of a point in 2D space.
    point_2: Coordinates of a point in 2D space.

    returns: int, distance of two point
    """
    
    return math.sqrt((point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2)

def point_in_circle(circle, point):
    """
    Check position of 1 point relative to circle

    circle: 1 circle with two parameters center and radius
    point: Coordinates of a point in 2D space.
    """
    
    if distance(circle.center, point) <= circle.radius:
        return True
    else:
        return False

class Rectangle:
    """
    Represents a rectangle with attributes conner, width, height.
    """
    
    def __init__(self, corner, width, height):
        """
        Initializes a rectangle object.

        conner (Point): The conner of the rectangle.
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        """
        
        self.corner = corner
        self.width = width
        self.height = height

def rect_in_circle(circle, rectangle):
    """
    Check position of 1 rectangle relative to circle

    circle: 1 circle with two parameters center and radius
    rectangle: 1 rectangle with 3 parameters conner, width, height
    """
    
    vertex = Point(rectangle.corner.x, rectangle.corner.y)

    if not point_in_circle(circle, vertex):
        return False

    vertex.x += rectangle.width
    if not point_in_circle(circle, vertex):
        return False

    vertex.y -= rectangle.height
    if not point_in_circle(circle, vertex):
        return False

    vertex.x -= rectangle.width
    if not point_in_circle(circle, vertex):
        return False

    return True

def rect_circle_overlap(circle, rectangle):
    """
    Check the position of the vertices of a rectangle relative to a circle

    circle: 1 circle with two parameters center and radius
    rectangle: 1 rectangle with 3 parameters conner, width, height
    """
    
    vertex = Point(rectangle.corner.x, rectangle.corner.y)

    if point_in_circle(circle, vertex):
        return True

    vertex.x += rectangle.width
    if point_in_circle(circle, vertex):
        return True

    vertex.y -= rectangle.height
    if point_in_circle(circle, vertex):
        return True

    vertex.x -= rectangle.width
    if point_in_circle(circle, vertex):
        return True

    return False

def main():
    circle_center = Point(150, 100)
    circle_radius = 75
    circle = Circle(circle_center, circle_radius)

    point = Point(160, 90)
    print(point_in_circle(circle, point))

    rectangle_corner = Point(500, 467)
    rectangle_width = 50
    rectangle_height = 30
    rectangle = Rectangle(rectangle_corner, rectangle_width, rectangle_height)
    print(rect_in_circle(circle, rectangle))
    print(rect_circle_overlap(circle, rectangle))
 
if __name__ == '__main__':
    main()
