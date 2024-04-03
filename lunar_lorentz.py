#!/usr/bin/env python3
# Jesse B. for mr5x5x5

import time
import threading
import moon_utils

def convert_earth_time_to_lunar(earth_time):
    # Applying the Lorentz time dilation formula to account for relativistic effects
    gamma = 1 - (30 ** 2) / (3e8 ** 2)
    lunar_time = earth_time / gamma
    return lunar_time

def display_running_clock():
    start_time = time.time()
    print(f"Time Started: {time.strftime('%I:%M:%S %p')}")

    while True:
        current_time = time.time()
        earth_time = current_time % 24
        lunar_time = convert_earth_time_to_lunar(earth_time)
        print_clock_info(current_time, earth_time, lunar_time)

        user_input = input("Press <enter> to stop the clock: ")
        if user_input.lower() == '':
            end_time = time.time()
            break

    duration = end_time - start_time
    print_duration(duration)
    print_lunar_differential(duration)

def print_clock_info(current_time, earth_time, lunar_time):
    print(f"Pacific Standard Time: {time.strftime('%I:%M:%S %p', time.localtime(current_time))}")
    print(f"Earth Time: {earth_time:.6f} | Lunar Time: {lunar_time:.6f}")

def print_duration(duration):
    minutes, seconds = divmod(duration, 60)
    seconds, microseconds = divmod(seconds, 1)
    microseconds = round(microseconds * 1e6)
    print(f"Duration of the clock running: {int(minutes)} minutes, {int(seconds)} seconds, {int(microseconds)} microseconds")

def print_lunar_differential(duration):
    # Calculate lunar duration based on earth duration
    duration_lunar = convert_earth_time_to_lunar(duration)
    print(f"Lunar differential: {duration_lunar:.6f} seconds")

# Separate the calculation and printing operations
clock_thread = threading.Thread(target=display_running_clock)
clock_thread.start()

# Wait for the clock to stop before continuing
clock_thread.join()
