#!/usr/bin/env python3

def garden_operations(s, test_type):
    if test_type == "ValueError":
        try:
            int(s)
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")

    elif test_type == "ZeroDivisionError":
        try:
            v = int(s)
            v /= 0
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")

    elif test_type == "FileNotFoundError":
        try:
            open("txt.txt", "r")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'txt.txt'\n")

    elif test_type == "KeyError":
        try:
            something = {"plant": "rose"}
            something[s]
        except KeyError:
            print(f"Caught KeyError: '{s}'\n")


def test_error_types():
    print("Testing ValueError...")
    garden_operations("abc", "ValueError")

    print("Testing ZeroDivisionError...")
    garden_operations("33", "ZeroDivisionError")

    print("Testing FileNotFoundError...")
    garden_operations("", "FileNotFoundError")

    print("Testing KeyError...")
    garden_operations("rose", "KeyError")

    print("Caught an error, but program continues!")


test_error_types()
