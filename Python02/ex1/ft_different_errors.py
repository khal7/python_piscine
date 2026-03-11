#!/usr/bin/env python3

def garden_operations() -> None:

    try:
        print("Testing ValueError...")
        x = int("abc")
        x
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        print(10 / 0)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    try:
        print("Testing FileNotFoundError...")
        f = open("missing.txt", 'r')
        f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        dict = {"rose": 1}
        print(dict["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")


def test_error_types() -> None:

    print("=== Garden Error Types Demo ===\n")
    garden_operations()

    try:
        print("Testing multiple errors together...")
        x = int("34")
        x
        print(10 / 0)
        f = open("missing.txt", 'r')
        f.close()
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
