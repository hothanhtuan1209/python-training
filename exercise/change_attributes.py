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
        
        minutes = hour * 60 + minute
        self.total_seconds = (minutes * 60) + second

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

    def time_to_int(self):
        """
        Computes the number of seconds since midnight
        """

        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        
        return seconds

    def is_after(self, other):
        """
        Returns True if t1 is after t2; false otherwise
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
        seconds = self.total_seconds + other.total_seconds
        
        return seconds

    def increment(self, seconds):
        """
        Returns a new Time that is the sum of this time and seconds.
        """

        increment_second = seconds + self.total_seconds

        return Time(increment_second)

    def is_valid(self):
        """
        Checks whether a Time object satisfies the invariants.
        """

        if self.total_seconds < 0:
            return False
        
        return True


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
    start = Time(9, 45, 00)
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
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == "__main__":
    main()
