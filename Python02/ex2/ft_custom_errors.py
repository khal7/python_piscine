#!/usr/bin/env python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def plant(plant: str, last_watering: int) -> None:
    if last_watering > 3:
        raise PlantError(f"The {plant} plant is wilting!")


def water(tank_volume: int) -> None:
    if tank_volume < 10:
        raise WaterError("Not enough water in the tank!")


def all_errors() -> None:
    print("\nTesting catching all garden errors...")
    i = 0
    for _ in (None, None):
        if i == 0:
            try:
                plant("tomato", 4)
            except GardenError as e:
                print(f"Caught a garden error: {e}")
        elif i == 1:
            try:
                water(1)
            except GardenError as e:
                print(f"Caught a garden error: {e}")
        i += 1


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("\ntesting PlantError...")
    try:
        plant("tomato", 4)
    except PlantError as e:
        print(f"Caught PlantError {e}")
    else:
        print("plant is fine")

    print("\nTesting WaterError...")
    try:
        water(9)
    except WaterError as e:
        print(f"Caught WaterError {e}")

    all_errors()
    print("\nAll custom error types work correctly!")
