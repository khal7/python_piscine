#!/usr/bin/env python3

def garden_operations(str):

    try:
        value = int(str)
        file = open(f"{str}", "r")
        value /= 0
        plants = {"name": "rose"}
        plants[str]

    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{str}'\n")
    except KeyError:
        print("Caught KeyError: '{str}'")


def test_error_types():
    print("Testing ValueError...")
    garden_operations("3")

    print("Testing ZeroDivisionError...")
    garden_operations("12")

    print("Testing FileNotFoundError...")
    garden_operations("txt.txt")

    print("Testing KeyError...")
    garden_operations("rose")

    print("Caught an error, but program continues!\n")


test_error_types()
