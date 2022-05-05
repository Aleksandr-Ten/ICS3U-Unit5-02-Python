#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: April 2022
# This program converts celsius to fahrenheit


def calculate_farenheit():
    # calculate farenheit

    # input
    c_temp_string = input("Enter a temperature (°C) : ")

    # process
    try:
        c_temp = int(c_temp_string)
        f_temp = round((c_temp * 9 / 5) + 32, 2)

        # output
        print("{0}°C is equal to {1}°F".format(c_temp, f_temp))
    except Exception:
        print("Invalid input. Please try again.")


def main():

    # this function just calls another function

    # call function
    calculate_farenheit()
    print("\nDone.")


if __name__ == "__main__":
    main()
