"""
This module contains a code for exercises 16-2 related to:
Think Python, 2nd Edition
Chapter 16: Classes and Functions

- Write a program that gets the current date and prints the day of the week.
- Write a program that takes a birthday as input and prints the user’s age and the
number of days, hours, minutes and seconds until their next birthday.
- Takes two birthdays and computes their Double Day.
- Write the more general version that computes the day when one person is n times older than the other.
"""

from datetime import datetime, timedelta

def print_current_day():
    """
    Get the current date and print day of week
    """
    
    day_of_week = (datetime.today().strftime('%A'))
    print(day_of_week)

def print_age(birthday_year, birthday_month, birthday_day):
    """
    Prints the user's age
    
    Parameters:
        birthday_year (int): year of birth
        birthday_month (int): month of birth
        birthday_day (int): day of birth

    returns (int): age of you
    """

    day_current = datetime.now()
    age = day_current.year - birthday_year - 1
    
    if birthday_month > day_current.month:
        return age
    
    if birthday_month < day_current.month:
        age += 1
        return age

    if birthday_month == day_current.month:
        if day_current.day >= birthday_day:
            age +=1
            return age

        if day_current.day < birthday_day:
            return age

def birthday_countdown(birthday_month, birthday_day):
    """
    Calculates time to next birthday

    Parameters:
        birthday_month (int): month of birth
        birthday_day (int): day of birth
    
    returns (daytime): time to next birthday 
    """
    
    current_date = datetime.now()
    next_birthday = datetime(current_date.year, birthday_month, birthday_day)

    if current_date > next_birthday:
        next_birthday = datetime(current_date.year + 1, birthday_month, birthday_day)

    time_to_next_birthday = next_birthday - current_date
    return time_to_next_birthday

def double_day(birthday_1, birthday_2):
    """
    Calculate the Double Day of two birthdays.

    Arguments:
        birthday_1 (datetime): The birthday of the first person.
        birthday_2 (datetime): The birthday of the second person.

    returns:
        datetime: the Double Day
    """
    
    if birthday_1 > birthday_2:
        birthday_1, birthday_2 = birthday_2, birthday_1

    diff = birthday_2 - birthday_1
    double_day = birthday_2 + diff

    return double_day

def n_times_older_day(birthday_1, birthday_2, ratio):
    """
    Calculate the day when one person is n times older than the other.

    Arguments:
        birthday_1 (datetime): The birthday of the first person.
        birthday_2 (datetime): The birthday of the second person.
        ratio (int): The ratio of age between the two persons (n times older).

    returns:
        datetime: The resulting day when the second person is n times older than the first.
    """
    
    if birthday_1 > birthday_2:
        birthday_1, birthday_2 = birthday_2, birthday_1

    target_age = ratio * (birthday_2 - birthday_1)
    ratio_times_older_day = birthday_2 + target_age

    return ratio_times_older_day

def main():
    print_current_day()

    print('Your age is:', print_age(2002, 5, 12))

    print('Next birthday will be in:', birthday_countdown(5, 12))

    birthday_input1 = input('Enter the birthday of the first person (format YYYY-MM-DD): ')
    birthday_input2 = input('Enter the birthday of the second person (format YYYY-MM-DD): ')
    ratio = int(input('Enter the age ratio: '))
    birthday_1 = datetime.strptime(birthday_input1, '%Y-%m-%d')
    birthday_2 = datetime.strptime(birthday_input2, '%Y-%m-%d')
    
    result_double = double_day(birthday_1, birthday_2)
    print('Double Day is:', result_double.strftime('%Y-%m-%d'))

    result_ratio = n_times_older_day(birthday_1, birthday_2, ratio)
    print('The day when one person is n times older than the other is', result_ratio.strftime('%Y-%m-%d'))

if __name__ == '__main__':
    main()
