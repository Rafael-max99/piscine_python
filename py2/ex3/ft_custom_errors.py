#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message
        super().__init__(self.message)

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)

def plant_errors() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilding!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

def water_errors() -> None:
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

def garden_errors() -> None:
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilding!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    plant_errors()
    print()
    water_errors()
    print()
    garden_errors()
    print()
    print("All custom error types work correctly!")
