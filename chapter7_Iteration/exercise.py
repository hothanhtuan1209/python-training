#Exercise 7-1
def mysqrt(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        return y 
import math
def math_sqrt():
    print('a     mysqrt(a)     math.sqrt(a)    diff')
    print('-     ----------   -------------    -----')
    a=1
    while 1<=a<10:
        result_mysqrt = mysqrt(a)
        result_mathsqrt = math.sqrt(a)
        diff = abs(result_mysqrt - result_mathsqrt)
        print(a,'   ',result_mysqrt,'   ',result_mathsqrt,'   ',diff)
        a+=1
math_sqrt()        

#Exercise 7-2:
def eval_loop():
    while True:
        input_values = input('enter an expression or done to finish: ')
        if input_values == 'done':
            break 
        else:
            result = eval(input_values)
            print(result)
eval_loop()