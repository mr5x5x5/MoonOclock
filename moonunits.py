#!/usr/bin/env python3
# Jesse B. for mr5x5x5

import datetime

def convert_earth_time_to_lunar(earth_time):
    # Define the time dilation effect due to the weaker gravitational pull of the Moon
    lunar_time = earth_time - 56e-6

    # Account for the subtle changes in the speed of a lunar clock based on its position on the lunar surface
    # Calculation for position-dependent speed change can be added here

    return lunar_time

def calculate_elapsed_time_delta(birthdate):
    # Define the birthdate
    birth_datetime = datetime.datetime.strptime(birthdate, "%Y-%m-%d")

    # Calculate the elapsed time since birth in seconds
    current_datetime = datetime.datetime.now()
    elapsed_time_delta = current_datetime - birth_datetime

    return elapsed_time_delta.total_seconds()

def convert_seconds_to_lunar_time(seconds):
    # Convert seconds to hours and adjust for the time dilation effect
    earth_time = seconds / 3600
    lunar_time = convert_earth_time_to_lunar(earth_time)

    return lunar_time

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
            elapsed_time_seconds = calculate_elapsed_time_delta(birthdate)
            lunar_time = convert_seconds_to_lunar_time(elapsed_time_seconds)
            break
        except ValueError:
            print("Invalid date format. Please enter your birthdate in YYYY-MM-DD format.")

    # Display the elapsed time since birth in seconds
    print(f"Elapsed time since birth: {elapsed_time_seconds} seconds")

    # Display the Lunar coordinated time
    print(f"Lunar coordinated time: {lunar_time:.6f} hours")

    # Draw the lunar landscape
    draw_lunar_landscape()

if __name__ == "__main__":
    main()
