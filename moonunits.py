#!/usr/bin/env python3
# Jesse B. for mr5x5x5

import datetime

def convert_earth_time_to_lunar(earth_time):
    """
    Convert Earth time to Lunar time considering the time dilation effect due to the weaker gravitational pull of the Moon.
    """
    lunar_elapsed_time = earth_time - (56e-6 * (earth_time / (24 * 3600)))  # Adjust for the time dilation effect
    return lunar_elapsed_time

def calculate_elapsed_lunar_time(birthdate):
    """
    Calculate the elapsed time in seconds since the birthdate until the current time.
    """
    birth_datetime = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
    current_datetime = datetime.datetime.now()
    elapsed_earth_time = (current_datetime - birth_datetime).total_seconds()
    return elapsed_earth_time

def draw_lunar_landscape():
    """
    Draw a simple lunar landscape using ASCII art.
    """
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
            lunar_elapsed_time = convert_earth_time_to_lunar(elapsed_time_seconds)
            break
        except ValueError:
            print("Invalid date format. Please enter your birthdate in YYYY-MM-DD format.")

    # Calculate the delta between Earth time and Coordinated Lunar Time
    delta = elapsed_time_seconds - lunar_elapsed_time

    # Display the output in two columns
    print(f"{'Time Elapsed (Earth)':<30}: {elapsed_time_seconds:.6f} seconds")
    print(f"{'Time Elapsed (Lunar)':<30}: {lunar_elapsed_time:.6f} seconds")
    print(f"{'Delta':<30}: {delta:.6f} seconds")

    # Draw the lunar landscape
    draw_lunar_landscape()

if __name__ == "__main__":
    main()

