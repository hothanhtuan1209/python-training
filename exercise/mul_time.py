"""
This module contains a code for exercises 16-1 related to:
Think Python, 2nd Edition
Chapter 16: Classes and Functions

- Write a function called mul_time that takes a Time object and a number and returns a
new Time object
- Use mul_time to write a function that takes a Time object that represents the
finishing time in a race, and a number that represents the distance, and returns a
Time object
"""

class Time:
    """
    Represents a circle with attributes center and radius.
    """
    
    def __init__(self, hour, minute, second):
        """
        Initializes a Time object.

        hour (int): The hour of time.
        minute (int): The minute of time.
        second (int): The second of time
        """
                
        self.hour = hour
        self.minute = minute
        self.second = second
    
def mul_time(time, number):
    """
    Multiplies a Time object by a given number.

    parameters:
        time (Time): The Time object to be multiplied.
        number (int or float): The number to multiply the Time object with.

    returns:
        Time: A new Time object
    """

    total_seconds = time.hour * 3600 + time.minute * 60 + time.second
    product_seconds = total_seconds * number

    new_hour = int(product_seconds // 3600)
    remaining_seconds = product_seconds - new_hour * 3600
    new_minute = int(remaining_seconds // 60)
    new_second = int(remaining_seconds - new_minute * 60)

    return Time(new_hour, new_minute, new_second)

def time_distance(finishing_time, distance):
    """
    Calculate average time per mile.

    parameters:
        finishing_time (Time): Time goes all the way.
        distance (int or float): The number represent distance

    returns:
        Time: A new Time object
    """

    total_seconds = finishing_time.hour * 3600 + finishing_time.minute * 60 + finishing_time.second
    time_race = total_seconds // distance

    hour_race = int(time_race // 3600)
    remaining_seconds_race = time_race - hour_race * 3600
    minute_race = int(remaining_seconds_race // 60)
    second_race = int(remaining_seconds_race - minute_race * 60)

    return Time(hour_race, minute_race, second_race)

def main():
    time = Time(2, 30, 45)
    number = 6.5
    result_time = mul_time(time, number)
    print(result_time.hour, ':', result_time.minute, ':',result_time.second)

    finishing_time = Time(1, 30, 15)
    distance = 50
    average_pace_time = time_distance(finishing_time, distance)
    print(average_pace_time.hour, ':', average_pace_time.minute, ':', average_pace_time.second)

if __name__ == '__main__':
    main()
