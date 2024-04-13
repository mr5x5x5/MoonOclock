#!/usr/bin/env python3
# Jesse B. for mr5x5x5

import datetime
import math

def calculate_time_elapsed_jupiter(birthdate):
    # Constants for Jupiter
    gravitational_constant = 6.674 * 10**-11  # Gravitational constant in m^3/kg/s^2
    mass_jupiter = 1.898 * 10**27  # Mass of Jupiter in kg
    radius_jupiter = 69911 * 10**3  # Radius of Jupiter in meters
    speed_of_light = 299792458  # Speed of light in m/s

    # Calculate the elapsed time since birth on Earth
    birth_datetime = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
    current_datetime = datetime.datetime.now()
    elapsed_time_earth = (current_datetime - birth_datetime).total_seconds()

    # Calculate the time dilation factor for Jupiter
    time_dilation_factor_jupiter = math.sqrt(1 - (2 * gravitational_constant * mass_jupiter) / (speed_of_light**2 * radius_jupiter))

    # Calculate the time elapsed on Jupiter
    time_elapsed_jupiter = elapsed_time_earth * time_dilation_factor_jupiter

    # Calculate the delta
    delta = elapsed_time_earth - time_elapsed_jupiter

    return time_elapsed_jupiter, delta
