#!/usr/bin/env python3
def check_temperature(temp_str) -> None:
    try:
        temp = int(temp_str)
        if temp >= 0 and temp <= 40:
            return f"Temperature {temp}°C is perfect for plants!\n"
        elif temp > 40:
            return f"Error: {temp}°C is too hot for plants (max 40°C)\n"
        elif temp < 0:
            return f"Error: {temp}°C is too cold for plants (min 0°C)\n"
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number\n"


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    temp_str = "25"
    print(f"Testing temperature: {temp_str}")
    print(check_temperature(temp_str))

    temp_str = "abc"
    print(f"Testing temperature: {temp_str}")
    print(check_temperature(temp_str))

    temp_str = "100"
    print(f"Testing temperature: {temp_str}")
    print(check_temperature(temp_str))

    temp_str = "-50"
    print(f"Testing temperature: {temp_str}")
    print(check_temperature(temp_str))

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
