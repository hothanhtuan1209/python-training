def is_palindrome(digits):
    """Check if a number is a palindrome."""
    if digits == digits[::-1]:
        return True
def check_odometer():
    """Find the numbers on the odometer that satisfy the requirements."""
    for number in range(100000, 1000000):
        digits = list(str(number))
        if is_palindrome(digits[2:]) or is_palindrome(digits[1:]) or is_palindrome(digits):
            print(number)
check_odometer()
