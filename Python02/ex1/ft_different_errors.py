#!/usr/bin/env python3


def garden_operations(s):

    try:
        value = int(s)
        value
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    try:
        v = int(s)
        v /= 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        file = open("txt.txt", "r")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'txt.txt'")

    try:
        something = {"plant": "rose"}
        something[s]
    except KeyError:
        print(f"Caught KeyError: '{s}'")

    print("Caught an error, but program continues!")


def test_error_types():
    print("Testing ValueError...")
    garden_operations("32")

    print("Testing ZeroDivisionError...")
    garden_operations("37")

    print("Testing FileNotFoundError...")
    # garden_operations("test.txt")

    print("Testing KeyError...")
    garden_operations("Tomato")


test_error_types()
