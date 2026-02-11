#!/usr/bin/env python3

class SecurePlant():
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, new_height):
        if new_height < 0:
            print(
                f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} [REJECTED]")
            print("Security: Negative age rejected")

        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def info(self):
        print(f"Plant created: {self.name}")

    def current_plant(self):
        print(
            f"Current plant: {self.name} ({self.__height}cm, {self.__age} days)")


print("=== Garden Security System ===")
rose = SecurePlant("Rose", 20, 10)
rose.set_height(25)
rose.set_age(30)
rose.set_height(-25)
rose.current_plant()
