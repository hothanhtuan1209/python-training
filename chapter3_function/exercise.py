#Exercise 3-1:
"""Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the 
string is in column 70 of the display:"""
def right_justify(s):
    spaces = " " * (70 - len(s))
    right_justify = spaces + s
    print(right_justify)
right_justify('Agility')

#Exercise 3-2:
"""1.A function object is a value you can assign to a variable or pass as an argument. For example, do_twice 
is a function that takes a function object as an argument and calls it twice:
   2. Modify do_twice so that it takes two arguments, a function object 
and a value,and calls the function twice, passing the value as an argument.
Use the modified version of do_twice to call print_twice twice,
passing 'spam' as an argument.
Define a new function called do_four that takes a function object 
and a value and calls the function four times, passing the value as a 
parameter. There should be only two statements in the body of this function, not four."""
def do_twice(f, values):
    f(values)
    f(values)
def print_twice(values):
    print(values)
    print(values)
do_twice(print_twice, 'spam')
def do_four(f, values):
    do_twice(f, values)
    do_twice(f,values)
do_four(print,'spam')

#Exercise 3-3:
# Write a function that draws a grid like the following:   
def ve_hangngang(a):
    print(a)
def ve_hangdoc(b):
    print(b)
    print(b)
    print(b)
    print(b)
a = "+ - - - - + - - - - +"
b = "|         |         |"
ve_hangngang(a)
ve_hangdoc(b)
ve_hangngang(a)
ve_hangdoc(b)
ve_hangngang(a)
