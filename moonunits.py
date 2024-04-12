#!/usr/bin/env python3
# Jesse B. for mr5x5x5

import datetime

def convert_earth_time_to_lunar(earth_time):
    # Define the time dilation effect due to the weaker gravitational pull of the Moon
    lunar_time = earth_time - 56e-6

    # Account for the subtle changes in the speed of a lunar clock based on its position on the lunar surface
    # Calculation for position-dependent speed change can be added here

    return lunar_time

def calculate_time_difference():
    # Prompt the user to enter their birthdate
    while True:
        try:
            earth_time_str = input("Enter the Earth time (HH:MM:SS): ")
            earth_time_parts = [int(part) for part in earth_time_str.split(":")]
            earth_time = earth_time_parts[0] + earth_time_parts[1]/60 + earth_time_parts[2]/3600
            break
        except ValueError:
            print("Invalid time format. Please enter the time in HH:MM:SS format.")

    # Calculate the difference between Coordinated Lunar Time and Earth time
    lunar_time = convert_earth_time_to_lunar(earth_time)
    time_difference = lunar_time - earth_time

    return time_difference

# Call the function to calculate the time difference and print the result
difference = calculate_time_difference()
print("Time Difference (Coordinated Lunar Time - Earth Time):", difference)
