import math

# Exercise 7-1
def mysqrt(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        return y 

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

# Exercise 7-2:
def eval_loop():
    while True:
        input_values = input('enter an expression or done to finish: ')
        if input_values == 'done':
            break 
        else:
            result = eval(input_values)
            print(result)
eval_loop()

# Exercise 7-3:
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def estimate_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        
        total += num / den
        term = factor * num/den
        
        if abs(term) < 1e-15:
            break
        k += 1
    return 1 / (factor * total)
print(estimate_pi())
print(math.pi)
