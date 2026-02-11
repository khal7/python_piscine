#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, aged):
        self.name = name
        self.height = height
        self.aged = aged

    def info(self):
        print(f"{self.name}: {self.height}cm, {self.aged} days old")

    def grow(self):
        self.height += 6

    def age(self):
        self.aged += 6


if __name__ == "__main__":

    rose = Plant("Rose", 25, 30)
    for day in range(1, 8, 6):
        rose_old_height = rose.height
        print(f"=== days {day} ===")
        rose.info()
        rose.grow()
        rose.age()
    print(f"Growth this week: +{rose.height - rose_old_height}")
