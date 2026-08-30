class Plant:
    def __init__(self, name: str, height: float, days: int, growth_value: float):
        self.name = name
        self._height = height
        self._days = days
        self.growth_value = growth_value

    @property
    def height(self) -> float:
        return self._height

    @property
    def days(self) -> int:
        return self._days

    @property
    def growth_value(self) -> float:
        return self._growth_value

    @height.setter
    def height(self, new_height: float):
        if new_height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height:.1f}cm")

    @days.setter
    def days(self, new_days: float):
        if new_days < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = new_days
            print(f"Age updated: {self._days:.1f} days")

    @growth_value.setter
    def growth_value(self, new_growth: float):
        if new_growth < 0:
            print(f"{self.name.capitalize()}: Error, growth value can't be negative")
            print("Growth value update rejected")
        else:
            self._growth_value = new_growth

    def show(self):
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.days} days old")

    def grow(self, days_passed: int):
        self.height += self.growth_value * days_passed

    def age(self, days_passed: int):
        self.grow(days_passed)
        self.days += days_passed


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("rose", 15, 10, 0.8)
    print("Plant created: ", end="")
    plant.show()
    print("")
    plant.height = 25
    plant.days = 30
    print("")
    plant.height = -5
    plant.days = -10
    print("\nCurrent state: ", end="")
    plant.show()
