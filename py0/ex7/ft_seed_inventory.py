#!/usr/bin/python3

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        mg = f"{seed_type.capitalize()} seeds: {quantity} packets available"
    elif unit == "grams":
        mg = f"{seed_type.capitalize()} seeds: {quantity} grams total"
    elif unit == "area":
        mg = f"{seed_type.capitalize()} seeds: covers {quantity} square meters"
    else:
        mg = "Unknown unit type"
    print(mg)
