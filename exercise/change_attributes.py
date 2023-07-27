"""
This module contains a code for exercises 17-1 related to:
Think Python, 2nd Edition
Chapter 17: Classes and Methods
Modify the methods (and the function int_to_time) to work with the
new implementation.
"""

class Time(object):
    """
    Represents the time of day.
    """

    def __init__(self, hour = 0, minute = 0, second = 0):
        """
        Initializes a Time object.

        Parameter:
            hour (int): The hour of the time (default is 0).
            minute (int): The minute of the time (default is 0).
            second (int): The second of the time (default is 0).
        """
        
        self.hour = hour
        self.minute = minute
        self.second = second
        minutes = hour * 60 + minute
        self.total_seconds = minutes * 60 + second

    def __str__(self):
        """
        Returns a string representation of the Time object in the form 'hour:minute:second'.

        Returns:
            str: A formatted string representing the time.
        """
        
        minutes, second = divmod(self.total_seconds, 60)
        hour, minute = divmod(minutes, 60)
        
        return "%.2d:%.2d:%.2d" % (hour, minute, second)

    def print_time(self):
        """
        Prints the time in the form of an integer representing the total seconds.
        """
        
        print(str(self.total_seconds))

    def is_after(self, other):
        """
        Checks if the time represented by this Time object is after the time represented by another Time object.

        other: Time object or number of seconds

        Returns:
            bool: True if the time represented by this Time object is after the time represented by the 'other' Time object, False otherwise.
        """
    
        return self.total_seconds > other.total_seconds

    def __add__(self, other):
        """
        Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """

        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """
        Adds two Time objects or a Time object and a number
        """

        return self.__add__(other)

    def add_time(self, other):
        """
        Adds two time objects
        """

        assert self.is_valid() and other.is_valid()
        total_seconds = self.total_seconds + other.total_seconds
        
        return int_to_time(total_seconds)

    def increment(self, seconds):
        """
        Returns a new Time that is the sum of this time and seconds.
        """

        increment_second = seconds + self.total_seconds
        
        if self.is_valid():
            return int_to_time(increment_second)
        else:
            raise ValueError("Invalid time.")

    def is_valid(self):
        """
        Checks whether a Time object satisfies the invariants.
        """

        if 0 <= self.hour <=23 and 0 <= self.minute <= 59 and 0 <= self.second <= 59:
            return True
        
        return False

def int_to_time(seconds):
    """
    Makes a new Time object.

    seconds: int seconds since midnight.
    """
    
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    
    return time

def main():
    start = Time(11, 45, 00)
    print("Start time")
    start.print_time()

    print("Time after increment of 1337 seconds")
    end = start.increment(1337)
    end.print_time()

    print("Is end after start?")
    print(end.is_after(start))

    print("Using _str_")
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print("Example of polymorphism")
    time_1 = Time(7, 43, 44)
    time_2 = Time(7, 41, 55)
    total = sum([time_1, time_2])
    print(total)

if __name__ == "__main__":
    main()
    