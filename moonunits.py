#!/usr/bin/env python3
# Jesse B. for mr5x5x5

import datetime

def calculate_age_delta():
    # Prompt the user to enter their birthdate
    while True:
        try:
            birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
            birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter your birthdate in YYYY-MM-DD format.")

    # Calculate the delta between the birthdate and the current date
    current_date = datetime.datetime.now()
    age_delta = current_date - birthdate

    return age_delta

# Call the function to calculate the age delta and print the result
delta = calculate_age_delta()
print("Your age delta:", delta)
