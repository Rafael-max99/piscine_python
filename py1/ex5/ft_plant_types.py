#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, height):
        if height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age):
        if age < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def show(self):
        return (f"{self.name.capitalize()}: {self._height}cm, {self._age} days old")

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def get_color(self):
        return self.color

    def bloom(self):
        self.has_bloomed = True
        print(f"{self.name.capitalize()} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_trunk_diameter(self):
        return self.trunk_diameter

    def produce_shade(self):
        print(f"Tree {self.name.capitalize()} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")

class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_values: int):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_values = nutritional_values

    def get_harvest_season(self):
        return self.harvest_season

    def get_nutritional_value(self):
        return self.nutritional_values

    def grow(self):
        self._height = round(self._height + 2.1, 1)

    def age(self):
        self._age += 1
        self.nutritional_values += 1

if __name__ == "__main__":
    rose = Flower("rose", 15.0, 10, "red")
    oak = Tree("oak", 200.0, 365, 5.0)
    tomato = Vegetable("tomato", 5.0, 10, "Abril", 0)

    print("=== Garden Plant Ttpes ===")

    print("=== Flower")
    print(f"{rose.show()}")
    print(f"Color: {rose.get_color()}")

    rose.bloom()

    print("")
    print("=== Tree")
    print(f"{oak.show()}")
    print(f"Trunk diameter: {oak.get_trunk_diameter()}cm")
    oak.produce_shade()

    print("")
    print("=== Vegetable")
    print(f"{tomato.show()}")
    print(f"Harvest season: {tomato.get_harvest_season()}")
    print(f"Nutritional value: {tomato.get_nutritional_value()}")
    for i in range(20):
        tomato.grow()
        tomato.age()
    print(f"{tomato.show()}")
    print(f"Harvest season: {tomato.get_harvest_season()}")
    print(f"Nutritional value: {tomato.get_nutritional_value()}")

