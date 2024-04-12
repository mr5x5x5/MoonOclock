#!/usr/bin/env python3
# Jesse B. for mr5x5x5

import datetime

def convert_earth_time_to_lunar(earth_time):
    # Define the time dilation effect due to the weaker gravitational pull of the Moon
    lunar_time_diff = earth_time - 56e-6

    # Account for the subtle changes in the speed of a lunar clock based on its position on the lunar surface
    # Calculation for position-dependent speed change can be added here

    return lunar_time_diff

def calculate_elapsed_lunar_time(birthdate):
    # Define the birthdate
    birth_datetime = datetime.datetime.strptime(birthdate, "%Y-%m-%d")

    # Calculate the elapsed time since birth in seconds
    current_datetime = datetime.datetime.now()
    elapsed_lunar_time = current_datetime - birth_datetime

    return elapsed_lunar_time.total_seconds()

def convert_seconds_to_lunar_time_diff(seconds):
    # Convert seconds to hours and adjust for the time dilation effect
    earth_time = seconds / 3600
    lunar_time_diff = convert_earth_time_to_lunar(earth_time)

    return lunar_time_diff

def draw_lunar_landscape():
    landscape = [
        "           .-~~~-.",
        "     .-~~~`.'| |`.~~~-.",
        "   .'~ ~ /`../ | \\..`\\ ~ ~`.",
        " .~`   .`/ |  | |  | \\`.   `~.",
        "/`~  .`/  |  | |  | |  \\`.  ~`\\",
    ]
    print("\n".join(landscape))

def main():
    # Prompt the user to enter their birthdate
    while True:
        try:
            birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
            elapsed_time_seconds = calculate_elapsed_lunar_time(birthdate)
            lunar_time_diff = convert_seconds_to_lunar_time_diff(elapsed_time_seconds)
            break
        except ValueError:
            print("Invalid date format. Please enter your birthdate in YYYY-MM-DD format.")

    # Calculate the delta between Earth time and Coordinated Lunar Time
    delta = elapsed_time_seconds - lunar_time_diff

    # Display the output in two columns
    print(f"{'Time Elapsed (Earth)':<30}: {elapsed_time_seconds:.6f} seconds")
    print(f"{'Time Elapsed (Lunar)':<30}: {delta:.6f} seconds")
    print(f"{'Delta':<30}: {lunar_time_diff:.6f} seconds")

    # Draw the lunar landscape
    draw_lunar_landscape()

if __name__ == "__main__":
    main()
