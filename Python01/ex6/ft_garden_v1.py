
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.color = ""
        self.prize_points = 0

    def info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class GardenManager:

    Plants = []
    print("=== Garden Management System Demo ===\n")

    def __init__(self, garden_owner):
        self.garden_owner = garden_owner
        GardenManager.Plants = GardenManager.Plants + [self]
        self.added_plant()

    def added_plant(self):
        print(f"Added {self.name} to {self.garden_owner}'s garden")

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    @classmethod
    def create_garden_network(cls):
        print(f"{cls.Plants[0].garden_owner} is helping all plants grow...")
        for plant in cls.Plants:
            plant.grow()
        print("\n")


# Garden report


    class GardenStats:
        @staticmethod
        def stats():
            print(
                f"=== {GardenManager.Plants[0].garden_owner}'s Gardn Report ===")
            print("Plants in garden:")
            count = 0
            regular = 0
            flowering = 0
            prize = 0
            valid = True
            scores = {}
            for plant in GardenManager.Plants:
                count += 1
                line = f"- {plant.name}: {plant.height}cm"
                if plant.height <= 0:
                    valid = False
                if plant.prize_points != 0:
                    prize += 1
                    line += f", {plant.color} flowers (blooming), Prize points: {plant.prize_points}"
                elif plant.color != "":
                    flowering += 1
                    line += f", {plant.color} flowers (blooming)"
                else:
                    regular += 1
                print(line)
                owner = plant.garden_owner
                if owner not in scores:
                    scores[owner] = 0
                scores[owner] += plant.height + plant.prize_points

            print(f"Plants added: {count}, Total growth: {count}cm")
            print(
                f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")
            print(f"Height validation test: {valid}")
            first = True
            print("Garden scores - ", end="")
            for owner in scores:
                if not first:
                    print(", ", end="")
                print(f"{owner}: {scores[owner]}", end="")
                first = False
            print()

            # total gardens managed
            total_gardens = 0
            for _ in scores:
                total_gardens += 1
            print(f"Total gardens managed: {total_gardens}")


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_point):
        super().__init__(name, height, age, color)
        self.prize_points = prize_point
