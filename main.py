#!/usr/bin/env python3
# Jesse B. for mr5x5x5

import time
import threading
import moon_utils


def convert_earth_time_to_lunar(earth_time):
  lunar_time = earth_time - 56e-6
  return lunar_time


def display_running_clock():
  start_time = time.time()
  print(
      f"Time Started: {time.strftime('%I:%M:%S %p', time.localtime(start_time))}"
  )

  while True:
    current_time = time.time()
    local_time = time.localtime(current_time)
    earth_time = local_time.tm_hour + local_time.tm_min / 60 + local_time.tm_sec / 3600
    lunar_time = convert_earth_time_to_lunar(earth_time)
    print_clock_info(current_time, earth_time, lunar_time)

    user_input = input("Press <enter> to stop the clock: ")
    if user_input.lower() == '':
      end_time = time.time()
      print(
          f"Time Ended: {time.strftime('%I:%M:%S %p', time.localtime(end_time))}"
      )
      break

  duration = end_time - start_time
  print_duration(duration)
  print_lunar_differential(duration)


def print_clock_info(current_time, earth_time, lunar_time):
  pacific_standard_time = time.strftime('%I:%M:%S %p',
                                        time.localtime(current_time))
  print(f"Pacific Standard Time: {pacific_standard_time}")
  print(f"Earth Time: {earth_time:.6f} | Lunar Time: {lunar_time:.6f}")


def print_duration(duration):
  minutes, seconds = divmod(duration, 60)
  seconds, microseconds = divmod(seconds, 1)
  microseconds = round(microseconds * 1e6)
  print(
      f"Duration of the clock running: {int(minutes)} minutes, {int(seconds)} seconds, {int(microseconds)} microseconds"
  )


def calculate_duration(duration_time):
  minutes, seconds = divmod(duration_time * 3600, 60)
  seconds, microseconds = divmod(seconds, 1)
  microseconds = round(microseconds * 1000000)
  return int(minutes), int(seconds), int(microseconds)


def print_lunar_differential(duration):
  duration_lunar = convert_earth_time_to_lunar(duration)
  print(f"Lunar differential: {duration_lunar:.6f} seconds")


# Separate the calculation and printing operations
clock_thread = threading.Thread(target=display_running_clock)
clock_thread.start()

# Wait for the clock to stop before continuing
clock_thread.join()
