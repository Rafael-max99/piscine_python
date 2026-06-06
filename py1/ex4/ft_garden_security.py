#!/usr/bin/python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
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
        m = f"{self.name.capitalize()}: {self._height}cm, {self._age} days old"
        print(m)


if __name__ == "__main__":

    """Define plant parameters"""
    rose = Plant("rose", 15.0, 10)

    """Show values of the plant"""
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()

    """Change values"""
    rose.set_height(25)
    rose.set_height(-25)
    rose.set_age(30)

    """Show data"""
    print(f"Height updated: {rose.get_height()}cm")
    print(f"Age updated: {rose.get_age()} days")
    print("")

    """Current State"""
    print("Current state: ", end="")
    rose.show()
