#!/usr/bin/python3

class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message
        super().__init__(message)

def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {plant_name}: [OK]")

def test_watering_system() -> None:
    plants1 = ["Tomato", "Lettuce", "Carrots"]
    plants2 = ["Tomato", "lettuce", "Carrots"]
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()
