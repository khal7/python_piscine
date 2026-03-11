#!/usr/bin/env python3

import sys
import math


def fun(positions: tuple | str) -> None:
    starting = (0, 0, 0)
    x1, y1, z1 = starting

    i = 0
    flag = 1
    try:
        string_coordinat = positions
        positions = positions.split(",")
        for element in positions:
            positions[i] = int(element)
            i += 1
    except AttributeError:
        flag = 0
        pass
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{string_coordinat}\"")
        print(f"Error prsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)")
        return
    positions = tuple(positions)
    x, y, z = positions
    if flag:
        print(f"Parsing coordinates: \"{string_coordinat}\"")
        print(f"Parsed position: {positions}")
    else:
        print(f"Position created: {positions}")
#    print(positions)
    result = math.sqrt((x - x1) ** 2 + (y - y1) ** 2 + (z - z1 ** 2))
    print(f"Distance between {starting} and {positions}: {result:.2f}\n")


def testing() -> None:
    print("=== Game Coordinate System ===\n")

    tup = (10, 20, 5)
    fun(tup)

    string_cordinations = "3,4,0"
    fun(string_cordinations)

    Invalid_coordinations = "abc,def,ghi"
    fun(Invalid_coordinations)

    x, y, z = tup1 = (3, 4, 0)
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    testing()
