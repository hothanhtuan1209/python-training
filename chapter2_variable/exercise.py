#Exercises 2-1.
"""1. We’ve seen that n = 42 is legal. What about 42 = n?
The program will report a syntax error"""
#42 = n SyntaxError

""""2.How about x = y = 1?
Program that assigns the value 1 to both x and y"""
x=y=1
print(x,y)

""""3. In some languages every statement ends with a semicolon, ;. What
happens if you put a semicolon at the end of a Python statement?
The program is still running normally """
print(x);

""""What if you put a period at the end of a statement?
The program will report a syntax error"""
# print(x). SyntaxError


#Exercises 2-1.

""""1.The volume of a sphere with radius r is 4/3πr3. 
What is the volume of a sphere with radius 5? if pi=3.14"""
x=3.14
y=5**3
print(x*y*4/3)

"""2.Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. 
What is the total wholesale cost for 60 copies?"""
24.95 * 60/100
14.97 * 60
3 + 59*0.75
898.2 + 47.25

"""If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and
1 mile at an easy pace again, what time do I get home for breakfast?"""
8 * 60 + 15 #second
7 * 60 + 12 #second
496*2 + 432*3 # = 38 minutes 6 seconds
