#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 04, 23, 2025
# This program is number guessing program with break statement.

import random


def main():
    # Generates random number from 0 to 9
    random_number = random.randint(0, 9)
    # I put the value to user_number as this because the loop couldn't work without the value of user_number.
    user_number = ""
    # While true loop with boolean expression.
    while user_number != random_number:
        # Gets the inpu
        user_number = input("Enter any number from 0 to 9.")
        try:
            user_number = int(user_number)
            print(f"{user_number} is incorrect, try again.")
            if user_number == random_number:
                print(f"You guessed the number, the number was {random_number}")
                break
        except Exception:
            print("Number should be integer.")


if __name__ == "__main__":
    main()
