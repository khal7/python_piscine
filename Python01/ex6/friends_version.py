#!/usr/bin/env python3

from ex1.ft_garden_data import Plant

# -------------------------------
# Plant hierarchy
# -------------------------------


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.type = "flower"
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, award):
        super().__init__(name, height, flower_color)
        self.award = award
        self.type = "prize flower"


class Tree(Plant):
    def __init__(self, name, height):
        super().__init__(name, height)
        self.type = "tree"


class Vegetable(Plant):
    def __init__(self, name, height):
        super().__init__(name, height)
        self.type = "vegetable"

# -------------------------------
# Garden Manager
# -------------------------------


class GardenManager:
    gardens = []  # tracks all garden instances (multiple gardens)

    class GardenStats:
        def __init__(self):
            self.total_plants = 0
            self.num_flowers = 0
            self.num_trees = 0
            self.num_vegetables = 0
            self.total_growth = 0

        def add_plant(self, plant):
            self.total_plants += 1
            if plant.type == "flower":
                self.num_flowers += 1
            elif plant.type == "tree":
                self.num_trees += 1
            elif plant.type == "vegetable":
                self.num_vegetables += 1

        def update_growth(self, growth):
            self.total_growth += growth

    def __init__(self, name):
        self.name = name
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens.append(self)  # add to class-level gardens list

    # instance method
    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.add_plant(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    # instance method
    def grow_plants(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            self.stats.update_growth(1)
            info = f"{plant.name} grew 1cm"
            if hasattr(plant, "is_blooming") and plant.is_blooming:
                info += f", {plant.flower_color} flowers (blooming)"
            print(info)

    # instance method
    def garden_report(self):
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            line = f"- {plant.name}: {plant.height}cm"
            if hasattr(plant, "flower_color"):
                line += f", {plant.flower_color} flowers"
            if hasattr(plant, "award"):
                line += f", Prize points: {plant.award}"
            print(line)
        print(
            f"Plants added: {self.stats.total_plants}, "
            f"Total growth: {self.stats.total_growth}cm"
        )
        print(
            f"Plant types: {self.stats.num_trees} regular, "
            f"{self.stats.num_flowers} flowering, "
            f"{self.stats.num_vegetables + self.stats.num_flowers} prize flowers"
        )

    # class method
    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {len(cls.gardens)}")
        return cls.gardens

    # static method
    @staticmethod
    def utility_message(msg):
        print(f"[UTILITY] {msg}")


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    # Create gardens
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    # Add plants
    alice_garden.add_plant(Tree("Oak", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    # Grow plants
    alice_garden.grow_plants()

    # Garden report
    alice_garden.garden_report()

    # Class method demo
    GardenManager.create_garden_network()

    # Static method demo
    GardenManager.utility_message("All gardens updated successfully.")
