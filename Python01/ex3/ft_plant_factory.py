#!/usr/bin/env python3
from ex2.ft_plant_growth import Plant


class createdPlants(Plant):
    def crt(self):
        print(f"Created: {self.name} ({self.height}cm, {self.aged} days)")


Rose = createdPlants("Rose", 25, 30)
Oak = createdPlants("Oak", 200, 365)
Cactus = createdPlants("Cactus", 5, 90)
Sunflower = createdPlants("Sunflower", 80, 45)
Fern = createdPlants("Fern", 15, 120)
plants = [Rose, Oak, Cactus, Sunflower, Fern]
print("=== Plant Factory Output ===")
n = 0
for plant in plants:
    n += 1
    plant.crt()
print(f"Total plants created: {n}")
