#!/usr/bin/env python3
# Jesse B. for mr5x5x5

# File: moon_utils.py
def moon_oclock(earth_time):
    # Define the time dilation effect due to the weaker gravitational pull of the Moon
    lunar_time = earth_time - 56e-6

    # Account for the subtle changes in the speed of a lunar clock based on its position on the lunar surface
    # Calculation for position-dependent speed change can be added here

    return lunar_time

def earth_to_lorentz(earth_time):
    # Applying the Lorentz time dilation formula to account for relativistic effects
    gamma = 1 - (30 ** 2) / (3e8 ** 2)
    lunar_time = earth_time / gamma
    return lunar_time
