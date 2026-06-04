#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.days} days old")

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)

    rose.show()
    sunflower.show()
    cactus.show()
