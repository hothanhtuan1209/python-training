def is_palindrome(digits):
    """Check if a number is a palindrome"""
    if digits == digits[::-1]:
        return True
    
def check_odometer():
    for number in range(100000, 1000000):
        # Convert number to list
        digits = list(str(number))

        # Call function is_palindrome to check condition
        if is_palindrome(digits[2:]) or is_palindrome(digits[1:]) or is_palindrome(digits):
            print(number)
            
check_odometer()
