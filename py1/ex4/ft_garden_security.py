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

if __name__ == "__main__":
    """Define plant parameters"""
    rose = Plant("rose", 15.0, 10)

    """Show values of the plant"""
    print("=== Garden Security System ===")
    print(f"Plant created: {rose.show()}\n")

    """Change values"""
    rose.set_height(10)
    rose.set_height(-25)
    rose.set_age(5)

    """Show data"""
    print(f"Height update: {rose.get_height()}cm")
    print(f"Age update: {rose.get_age()} days")
    print("")

    """Current State"""
    print(f"Current state: {rose.show()}")







