#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program adds positive integers and uses a continue statement


def main():
    # This function adds the numbers
    loop_counter = 0
    answer = 0

    # Input
    print("This program adds together positive integers.")
    number_as_string = input("Enter the number of integers you would "
                             "like to add: ")

    # Process & Output
    while True:
        try:
            number_as_integer = int(number_as_string)

            print("")
            break

        except Exception:
            number_as_string = input("{} is not a valid input. Enter the "
                                     "number of integers you would like to "
                                     "add: ".format(number_as_string))

    for loop_counter in range(number_as_integer):
        entered_integers_string = input("Enter an integer to add: ")

        try:
            entered_integers_integer = int(entered_integers_string)

            if entered_integers_integer < 0:
                continue
            else:
                answer = answer + entered_integers_integer

        except Exception:
            print("Invalid input.")
    print("")
    print("The sum of all the positive integers is: {}".format(answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
