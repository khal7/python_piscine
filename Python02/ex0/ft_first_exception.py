#!/usr/bin/env python3
def check_temperature(value):

    try:
        temp = int(value)
        if temp >= 0 and temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!\n")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
    except:
        ValueError
        print(f"Error: '{value}' is not a valid number\n")


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")

    value = "25"
    print(f"Testing temperature: {value}")
    check_temperature(value)

    value = "abc"
    print(f"Testing temperature: {value}")
    check_temperature(value)

    value = "100"
    print(f"Testing temperature: {value}")
    check_temperature(value)

    value = "-50"
    print(f"Testing temperature: {value}")
    check_temperature(value)

    print("All tests completed - program didn't crash!")


test_temperature_input()
