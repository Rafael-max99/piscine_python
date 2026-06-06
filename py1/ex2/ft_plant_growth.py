#!/usr/bin/python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.initial_height = height

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self._age += 1

    def total_growth(self) -> float:
        return round(self.height - self.initial_height, 1)

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: {self.height}cm, {self._age} days old"
        )


if __name__ == "__main__":

    print("=== Garden Plant Growth ===")

    rose = Plant("rose", 25.0, 30)

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.show()
        rose.grow()
        rose.age()

    print(f"Growth this week: {rose.total_growth()}cm")
