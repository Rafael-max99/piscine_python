#!/usr/bin/python3


from alchemy.potions import strength_potion
from ..elements import create_air
from elements import create_fire


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' and "
            f"'{strength_potion()}' mixed with '{create_fire()}'")


if __name__ == "__main__":
    print(lead_to_gold())
