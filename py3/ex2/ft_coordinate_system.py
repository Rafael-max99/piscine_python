#!/usr/bin/python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        values = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = values.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords = []

        for part in parts:
            part = part.strip()
            try:
                coords.append(float(part))
            except ValueError:
                print(
                    f"Error on parameter '{part}': "
                    f"could not convert string to float: '{part}'"
                    )
                break
        else:
            return (coords[0], coords[1], coords[2])


def distance_to_center(pos: tuple[float, float, float]) -> float:
    x, y, z = pos
    return math.sqrt(x**2 + y**2 + z**2)


def distance_between(
        pos1: tuple[float, float, float],
        pos2: tuple[float, float, float]
        ) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    coord1 = get_player_pos()
    print(f"Got a first tuple: {coord1}")
    print(f"It includes: X={coord1[0]}, Y={coord1[1]}, Z={coord1[2]}")
    dist_to_center = round(distance_to_center(coord1), 4)
    print(f"Distance to center: {dist_to_center}")

    print("Get a second set of coordinates")
    coord2 = get_player_pos()
    dist_between_them = round(distance_between(coord1, coord2), 4)
    print(f"Distance between the 2 sets of coordinates: {dist_between_them}")
