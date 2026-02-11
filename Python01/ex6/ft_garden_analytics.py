#!/usr/bin/env python3

from ex1.ft_garden_data import Plant

# -------------------
# Plant hierarchy
# -------------------


class FloweringPlant(Plant):
    def __init__(self, name, height, age, flower_color):
        super().__init__(name, height, age)
        self.flower_color = flower_color
        self.type = "flower"
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, flower_color, award):
        super().__init__(name, height, age, flower_color)
        self.award = award
        self.type = "prize flower"


class Tree(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
        self.type = "tree"


class Vegetable(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
        self.type = "vegetable"

# -------------------
# Garden Manager
# -------------------


class GardenManager:
    gardens = []

    class GardenStats:
        def __init__(self):
            self.total_plants = 0
            self.num_trees = 0
            self.num_flowers = 0
            self.num_prize_flowers = 0
            self.total_growth = 0

        def add_plant(self, plant):
            self.total_plants += 1
            if isinstance(plant, PrizeFlower):
                self.num_prize_flowers += 1
            elif isinstance(plant, FloweringPlant):
                self.num_flowers += 1
            elif isinstance(plant, Tree):
                self.num_trees += 1

        def update_growth(self, growth):
            self.total_growth += growth

    def __init__(self, name):
        self.name = name
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens.append(self)

    # -------------------
    # Instance methods
    # -------------------
    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.add_plant(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_plants(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            self.stats.update_growth(1)
            info = f"{plant.name} grew 1cm"
            if hasattr(plant, "is_blooming") and plant.is_blooming:
                info += f", {plant.flower_color} flowers (blooming)"
            if hasattr(plant, "award"):
                info += f", Prize points: {plant.award}"
            print(info)

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
            f"{self.stats.num_prize_flowers} prize flowers"
        )

    # -------------------
    # Class method
    # -------------------
    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {len(cls.gardens)}")
        return cls.gardens

    # -------------------
    # Static method
    # -------------------
    @staticmethod
    def utility_message(msg):
        print(f"[UTILITY] {msg}")


# -------------------
# Example usage
# -------------------
if __name__ == "__main__":
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    # Make sure we include the age argument
    alice_garden.add_plant(Tree("Oak", 100, 1825))
    alice_garden.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, 51, "yellow", 10))

    alice_garden.grow_plants()
    alice_garden.garden_report()

    GardenManager.create_garden_network()
    GardenManager.utility_message("All gardens updated successfully.")
