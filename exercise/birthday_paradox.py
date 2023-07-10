"""
This module contains a code for exercises 10-8 related to:
Think Python, 2nd Edition
Chapter 10: Lists

If there are 23 students in your class, what are the chances that two
of you have thes same birthday? You can estimate this probability by 
generating random samples of 23 birthdays and checking for matches.
"""

import random

def has_duplicates(list_input):
    """
    Returns True if any element appears more than once in a sequence.

    list_input: list

    returns: bool
    """

    # make a copy of t to avoid modifying the parameter
    list_copy = list_input[:]
    list_copy.sort()

    # check for adjacent elements that are equal
    for i in range(len(list_copy)-1):
        if list_copy[i] == list_copy[i+1]:
            return True
    
    return False

def random_birthdays(num_student):
    """
    Create a list of integers between 1 and 365, with length n.

    n: int

    returns: list of int
    """

    birthday_random_list = []
    for i in range(num_student):
        birthday = random.randint(1, 365)
        birthday_random_list.append(birthday)
    
    return birthday_random_list

def count_matches(num_students, num_simulations):
    """
    Generates a sample of birthdays and counts duplicates.

    num_students: how many students in the group
    num_samples: how many groups to simulate

    returns count
    """

    count = 0
    for i in range(num_simulations):
        list_birthday_simulations = random_birthdays(num_students)
        
        if has_duplicates(list_birthday_simulations):
            count += 1
    
    return count

def main():
    """
    Runs the birthday simulation and prints the number of matches.
    """

    num_students = 23
    num_simulations = 500
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)

main()
