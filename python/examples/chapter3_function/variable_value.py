import math


signal_power = 4
noise_power = 5
ratio = signal_power / noise_power
decibels = 10*math.log10(ratio)
radians = 0.7
height = math.sin(radians)
