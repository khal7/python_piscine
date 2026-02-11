

class GardenManager:
    def __init__(self):
        self.gardens = []


class garden:
    def __init__(self, owner):
        self.plants = []
        self.owner = owner

    def get_plant(self, plant):
        self.plants = self.plants + [plant]

    def grow(self):
        self.height += 1

    def print_plants(self):
        for plant in self.plants:
            print(f"Added {plant.name} to {self.owner}'s garden")


class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name, height, color, blooming):
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, blooming, prize_points):
        super().__init__(name, height, color, blooming)
        self.prize_points = prize_points
