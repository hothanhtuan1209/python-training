"""
This module contains a code for exercises 15-2 related to:
Think Python, 2nd Edition
Chapter 15: Classes and Objects

- Write a function called draw_rect that takes a Turtle object and a Rectangle and uses
the Turtle to draw the Rectangle.
- Write a function called draw_circle that takes a Turtle and a Circle and draws the
Circle.
"""


import turtle
from circle_rectangle import Rectangle
from circle_rectangle import Circle
from circle_rectangle import Point


def draw_rect(turtle, rectangle):
    """
    Draws a rectangle using the Turtle.

    turtle: Turtle object
    rect: Rectangle object
    """

    turtle.penup()
    turtle.goto(rectangle.corner.x, rectangle.corner.y)
    turtle.pendown()

    for _ in range(2):
        turtle.forward(rectangle.width)
        turtle.left(90)
        turtle.forward(rectangle.height)
        turtle.left(90)


def draw_circle(turtle, circle):
    """
    Draws a circle using the Turtle.

    turtle: Turtle object
    circle: Circle object
    """

    turtle.penup()
    turtle.goto(circle.center.x, circle.center.y - circle.radius)
    turtle.pendown()
    turtle.circle(circle.radius)


def main():
    circle_center = Point(150, 100)
    circle_radius = 75
    circle = Circle(circle_center, circle_radius)

    rectangle_corner = Point(100, 80)
    rectangle_width = 50
    rectangle_height = 30
    rectangle = Rectangle(rectangle_corner, rectangle_width, rectangle_height)

    print(draw_rect(turtle, rectangle))
    print(draw_circle(turtle, circle))


if __name__ == '__main__':
    main()
