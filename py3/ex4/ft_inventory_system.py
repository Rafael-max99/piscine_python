#!/usr/bin/python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error- invalid parameter '{arg}'")
            continue

        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error- invalid parameter '{arg}'")
            continue

        item_name, quantity_str = parts

        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
            continue

        if item_name in inventory:
            print(f"Redundant item '{item_name}'- discarding")
            continue

        inventory[item_name] = quantity

    print(f"Got inventory: {inventory}")

    if not inventory:
        return

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    for item, quantity in inventory.items():
        percentage = (quantity / total_quantity) * 100
        print(f"Item {item} represents {round(percentage, 1)}%")

    most_abundant = list(inventory.keys())[0]
    least_abundant = list(inventory.keys())[0]
    for item, qty in inventory.items():
        if qty > inventory[most_abundant]:
            most_abundant = item
        if qty < inventory[least_abundant]:
            least_abundant = item
    print(
        f"Item most abundant: {most_abundant} "
        f"with quantity {inventory[most_abundant]}"
        )
    print(
        f"Item least abundant: {least_abundant} "
        f"with quantity {inventory[least_abundant]}"
        )

    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
