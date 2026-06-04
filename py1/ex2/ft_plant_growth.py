#!/usr/bin/python3

class Plant:
    def __init__(self, name , height, age):
        self.name = name
        self.height = height
        self.age = age
        self.initial_height = height

    def grow(self):
        self.height = round(self.height + 0.8, 1)

    def age_up(self):
        self.age += 1

    def total_growth(self):
        return round(self.height - self.initial_height)

    def show(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant("rose", 25.0, 30)

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.show()
        rose.grow()
        rose.age_up()

    print(f"Grow this week: {rose.total_growth()}cm")
