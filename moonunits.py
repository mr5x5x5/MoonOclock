#!/usr/bin/env python3
# Jesse B. for mr5x5x5

import datetime

def convert_earth_time_to_lunar(earth_time):
    # Define the time dilation effect due to the weaker gravitational pull of the Moon
    lunar_time = earth_time - 56e-6

    # Account for the subtle changes in the speed of a lunar clock based on its position on the lunar surface
    # Calculation for position-dependent speed change can be added here

    return lunar_time

def calculate_time_difference(birthdate):
    # Define the birthdate and noon time on that day
    birth_datetime = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
    noon_datetime = birth_datetime.replace(hour=12, minute=0, second=0)

    # Calculate the Earth time and Lunar coordinated time at noon on the birth day
    earth_time_noon = (noon_datetime - datetime.datetime(noon_datetime.year, noon_datetime.month, noon_datetime.day)).total_seconds() / 3600
    lunar_time_noon = convert_earth_time_to_lunar(earth_time_noon)

    # Calculate the current Earth time
    current_datetime = datetime.datetime.now()
    current_time = (current_datetime - datetime.datetime(current_datetime.year, current_datetime.month, current_datetime.day)).total_seconds() / 3600

    # Calculate the difference between Earth and Lunar coordinated time
    delta = current_time - lunar_time_noon

    return earth_time_noon, lunar_time_noon, delta

def draw_lunar_landscape():
    landscape = [
        "           ___-------___          ",
        "      _-~~                 ~~--_  ",
        "   _-~                           ~-_ ",
        "  /                                   \\",
        " /          ____           ____        \\",
        "/      /   /    \\  \\    /  /    \\   \\  \\",
    ]
    print("\n".join(landscape))

def main():
    # Prompt the user to enter their birthdate
    while True:
        try:
            birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
            birth_datetime = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
            birthdate_formatted = birth_datetime.strftime("%B %d, %Y")
            earth_time_noon, lunar_time_noon, delta = calculate_time_difference(birthdate)
            break
        except ValueError:
            print("Invalid date format. Please enter your birthdate in YYYY-MM-DD format.")

    # Display the data using columns
    print("\n\n")
    print(f"{'Birthdate':<20}: {birthdate_formatted}")
    print(f"{'Earth Time at Noon':<20}: {earth_time_noon:.6f} hours")
    print(f"{'Lunar Time at Noon':<20}: {lunar_time_noon:.6f} hours")
    print(f"{'Elapsed Time Delta':<20}: {delta:.6f} hours")

    # Draw the lunar landscape
    draw_lunar_landscape()

if __name__ == "__main__":
    main()
