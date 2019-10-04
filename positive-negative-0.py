#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program draws a background and two sprites on the pybadge


def main():

    user_number = int(input("Enter your number: "))
    if (user_number > 0):
        print("Your number is positive")
    elif (user_number < 0):
        print("Your number is negative")
    else:
        print("Your number is 0")


if __name__ == "__main__":
    main()
