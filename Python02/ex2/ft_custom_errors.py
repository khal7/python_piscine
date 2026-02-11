#!/usr/bin/env python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def plant():
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print("Caught PlantError:", e)


def water():
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print("Caught WaterError:", e)


print("=== Custom Garden Errors Demo ===\n")
print("Testing PlantError...")
plant()
print("Testing WaterError...")
water()
print("Testing catching all garden errors...")
try:
    plant()
    water()
except GardenError as e:
    print("Caught a garden error:", e)
print("All custom error types work correctly!")
