#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    for plant in plant_list:
        if plant == "":
            raise NameError("Error: Cannot water None - invalid plant!")
        else:
            print(f"Watering {plant}")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    normal_plants = ["tomato", "lettuce", "carrots"]
    error_plants = ["tomato", ""]
    lists = [normal_plants, error_plants]
    for list in lists:
        try:
            if list == normal_plants:
                print("Testing normal watering...")
            if list == error_plants:
                print("\nTesting with error...")
            water_plants(list)
        except NameError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")
            if list == normal_plants:
                print("Watering completed successfully!")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
