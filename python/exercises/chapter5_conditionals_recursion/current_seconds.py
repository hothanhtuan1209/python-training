"""
This code calculates and prints the current time in hours, minutes, and seconds
since the epoch (January 1, 1970) and the total number of days that have passed
since the epoch.

It uses the 'time' module to retrieve the current time in seconds and then
performs the necessary calculations to extract hours, minutes, and seconds
from the total seconds. It also calculates the total number of days.

The results are printed to the console.

This code provides information about the current time and the number of days
that have passed since the epoch.
"""


import time


print(time.time())
current_seconds = time.time()
total_days = current_seconds // (24 * 60 * 60)
seconds_left = current_seconds - total_days*24*60*60
hours = int(seconds_left // (60 * 60))
minutes = int((seconds_left % (60 * 60)) // 60)
second = int(seconds_left % 60)

# Result
print('The present time:', hours, ':', minutes, ':', second)
print('Number of days since epoch:', total_days)
