#!/usr/bin/python3

class Plant:
    @staticmethod
    def is_older_than_year(age) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self):
            print(f"Stats: {self.grow_count} grow, {self.age_count} age, {self.show_count} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)
        self._stats.grow_count += 1

    def age(self) -> None:
        self._age += 1
        self._stats.age_count += 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self._height}cm, {self._age} days old")
        self._stats.show_count += 1

    def get_stats(self) -> "Stats":
        return self._stats

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")

    def bloom(self):
        self.has_bloomed = True

class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.number_of_seeds = 0

    def show(self):
        super().show()
        print(f"Seeds: {self.number_of_seeds}")

    def bloom(self):
        super().bloom()
        self.number_of_seeds = 42

class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade_count = 0

        def display(self):
            super().display()
            print(f"{self.shade_count} shade")

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree.Stats()

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        

    def produce_shade(self):
        print(f"Tree {self.name.capitalize()} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")
        self._stats.shade_count += 1

def display_stats(plant: Plant):
    plant._stats.display()

if __name__ == "__main__":
    rose = Flower("rose", 15.0, 10, "red")
    oak = Tree("oak", 200.0, 365, 5.0)
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    anonymous_plant = Plant.create_anonymous()

    print("=== Garden statistics ===")
    print("Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    
    print()
    print("=== Flower")
    rose.show()
    display_stats(rose)
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)

    print()
    print("=== Tree")
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)

    print()
    print("=== Seed")
    sunflower.show()
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    print("")
    print("=== Anonymous")
    anonymous_plant.show()
    display_stats(anonymous_plant)
