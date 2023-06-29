#Exercise 5-1.
import time
print(time.time())

# Lấy thời gian hiện tại tính bằng giây kể từ epoch
so_giay_hien_tai = time.time()

# Tính số ngày(lấy số giây hiện tại chia lấy phần nguyên cho số giây của 1 ngày hoàn chỉnh)
tong_so_ngay = so_giay_hien_tai // (24 * 60 * 60)

# Số giây còn lại = tổng thời gian bỏ đi những ngày đã hoàn chỉnh(đủ 24*60*60 giây)
so_giay_con_lai =so_giay_hien_tai - tong_so_ngay*24*60*60

# Tính thời gian trong ngày theo giờ, phút và giây bằng số giây dư ra sau khi trừ các ngày hoàn chỉnh
gio = int(so_giay_con_lai // (60 * 60)) 
#lấy số giây chia lấy dư cho số giờ hoàn chỉnh để lấy ra giây sau đó tính phút
phut = int((so_giay_con_lai % (60 * 60)) // 60) 
#lấy số giây chia lấy dư cho số phút hoàn chỉnh để lấy ra giây
giay = int(so_giay_con_lai % 60)

# kết quả
print('Thời gian hiện tại:',gio,':',phut,':',giay)
print('Số ngày kể từ epoch:', tong_so_ngay)



#Exercise 5-2.
"""1. Write a function named check_fermat that takes four parameters—a, b, c and n and checks
to see if Fermat’s theorem holds. If n is greater than 2 and the program should print, “Holy smokes, 
Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.” """

def check_fermat(a,b,c,n):
        if n>2 and (a**n + b**n == c**n):
            print('Holy smokes, Fermat was wrong')
        else:
            print("no, that doesn't work")
check_fermat(4,5,7,3)

"""2. Write a function that prompts the user to input values for a, b, c and n, converts them to integers,
 and uses check_fermat to check whether they violate Fermat’s theorem"""
def check_fermat(a,b,c,n):
        if n>2 and (a**n + b**n == c**n):
            print('Holy smokes, Fermat was wrong')
        else:
            print("no, that doesn't work")
def input_check_fermat():
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    n = int(input('n='))
    check_fermat(a,b,c,n)
input_check_fermat()   


#Exercise 5-3.
"""1.Write a function named is_triangle that takes three integers as arguments, and that prints either “Yes” or “No”, 
depending on whether you can or cannot form a triangle from sticks with the given lengths."""
def is_triangle(a,b,c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print('No')
    else:
         print('Yes')
is_triangle(3,4,5)

"""2. Write a function that prompts the user to input three stick lengths, converts them to integers, and uses 
is_triangle to check whether sticks with the given lengths can form a triangle."""

def is_triangle():
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    if (a > b + c) or (b > a + c) or (c > a + b):
        print('No')
    else:
         print('Yes')
is_triangle()

#Exercise 5-4.
"""What is the output of the following program? Draw a stack diagram 
that shows the state of the program when it prints the result."""
"""_main_ 
recurse  (3-1, 0+3)
recurse  (2-1, 3+2)
recurse  (1-1, 5+1)
print 	6 
"""
"""1. What would happen if you called this function like this: recurse(-1, 0)?"""
"""Python reports an error message when the maximum recursion depth is reached"""

"""2. Write a docstring that explains everything someone would need to know in order 
to use this function (and nothing else)."""
"""To use this function, first you need to create a function with 2
parameters n and s, if n is 0 then print the value of s, if n is not 0, 
the function takes 2 new parameters as n-1 and n+s """