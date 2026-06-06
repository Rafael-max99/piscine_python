#!/usr/bin/python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, height) -> None:
        if height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age) -> None:
        if age < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: {self._height}cm, {self._age} days old"
        )


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def get_color(self) -> str:
        return self.color

    def bloom(self) -> None:
        self.has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_trunk_diameter(self) -> float:
        return self.trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
            )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, harvest_season: str, nutritional_values: int
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_values = nutritional_values

    def get_harvest_season(self) -> str:
        return self.harvest_season

    def get_nutritional_value(self) -> int:
        return self.nutritional_values

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_values}")

    def grow(self) -> None:
        self._height = round(self._height + 2.1, 1)

    def age(self) -> None:
        self._age += 1
        self.nutritional_values += 1


if __name__ == "__main__":

    rose = Flower("rose", 15.0, 10, "red")
    oak = Tree("oak", 200.0, 365, 5.0)
    tomato = Vegetable("tomato", 5.0, 10, "Abril", 0)

    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
