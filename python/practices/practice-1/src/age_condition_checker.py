"""
This exercise shows that the mother is 36 years older than the child,
when the child is 37 years old, the mother is 73 years old, the mother's
age is the opposite of the child's age, find the same cases as above
"""


def check_age(number):
    """
    Check the age condition for two people.

    This function takes an integer `number` as an age and checks if there
    exists another integer (its reverse) such that when added to `number`,
    the result is `36`.

    Parameters:
        - number (int): The age of the first person.
    """

    age_reverse = list(str(number))
    reversed_number = int(''.join(age_reverse[::-1]))

    if int(number) + 36 == reversed_number:
        print(number)


def reverse_age():
    """
    Check the age of pairs of people under certain conditions.

    This function iterates through numbers from 0 to 99 and checks if there
    exist pairs of people whose ages satisfy the condition in the `check_age`
    function.
    """

    for number in range(0, 100):
        # Convert all 1 digit numbers to 2 character strings
        add_number_0 = str(number).zfill(2)
        check_age(add_number_0)


reverse_age()
