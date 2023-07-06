"""
This lesson goes through all 6 digit numbers, prints the numbers
with the last 4 or last 5 digits or all 6 numbers that are symmetrical.
"""

def is_palindrome(digits):
    # Check if a number is a palindrome
    if digits == digits[::-1]:
        return True
    
def check_odometer():
    # Check last 4 numbers, last 5 numbers and 6 number
    for number in range(100000, 1000000):
        # Convert number to list
        digits = list(str(number))

        # Call function is_palindrome to check condition
        if is_palindrome(digits[2:]) or is_palindrome(digits[1:]) or is_palindrome(digits):
            print(number)

check_odometer()
