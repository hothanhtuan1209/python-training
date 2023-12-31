"""
This exercise shows that the mother is 36 years older than the child,
when the child is 37 years old, the mother is 73 years old, the mother's
age is the opposite of the child's age, find the same cases as above
"""

def check_age(number):
    # Check the age condition of 2 people
    # Convert number to list
    age_reverse = list(str(number))

    # Concatenate characters into strings, then convert to integers
    reversed_number = int(''.join(age_reverse[::-1]))

    # Check condition 
    if int(number) + 36 == reversed_number:
        print(number)

def reverse_age():
    for number in range(0, 100):
        # Convert all 1 digit numbers to 2 character strings
        add_number_0 = str(number).zfill(2)
        check_age(add_number_0)

reverse_age()
