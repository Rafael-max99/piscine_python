#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"Created: {self.name.capitalize()}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    plants = [
            Plant("rose", 25.0, 30),
            Plant("oak", 200.0, 365),
            Plant("cactus", 5.0, 90),
            Plant("sunflower", 80.0, 45),
            Plant("fern", 15.0, 120)
            ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.show()
