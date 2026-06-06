#!/usr/bin/python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, {self.age} days old"
        )


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
        print("Created: ", end="")
        plant.show()
