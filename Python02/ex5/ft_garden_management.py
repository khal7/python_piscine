#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sun: int):
        self.name = name
        self.water_level = water_level
        self.sun = sun


class GardenManager:
    def __init__(self, tank_volume: int) -> None:
        self.tank_volume = tank_volume
        self.plants = []

    def add_plant(self, plant: object) -> None:
        if plant.name == "":
            raise PlantError(
                "Error adding plant: Plant name cannot be empty!\n")

        self.plants.append(plant)
        print(f"Added {plant.name} successfully")

    def water_plant(self) -> None:
        for plant in self.plants:
            if plant.water_level < 1:
                raise WaterError("Not enough water")
            elif plant.water_level > 15:
                raise WaterError("Plant has too much water")
            print(f"Watering {plant.name} - success")

    def plant_health(self) -> None:
        for plant in self.plants:
            if plant.water_level > 10:
                raise WaterError(
                    f"Error check checking {plant.name}: Water "
                    f"level {plant.water_level} is too high (max 10)\n")
            print(
                f"{plant.name} healthy (water: {plant.water_level},"
                f" sun: {plant.sun})")

    def water_in_tank(self) -> None:
        if self.tank_volume < 1:
            raise GardenError("Caught GardenError: Not enough water in tank")


def test_garden_management() -> None:
    garden = GardenManager(0)
    print("=== Garden Management System ===\n")
    try:
        print("Adding plants to garden...")
        garden.add_plant(Plant("tomato", 5, 8))
        garden.add_plant(Plant("lettuce", 15, 9))
        garden.add_plant(Plant("", 3, 5))
    except PlantError as e:
        print(e)

    try:
        print("Watering plants...")
        print("Opening watering system")
        garden.water_plant()
    except WaterError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)\n")

    try:
        print("Checking plant health...")
        garden.plant_health()
    except WaterError as e:
        print(e)

    try:
        print("Testing error recovery...")
        garden.water_in_tank()
    except GardenError as e:
        print(e)
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
