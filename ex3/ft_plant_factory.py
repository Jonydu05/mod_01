class Plant:
    def __init__(self, name: str, height: float, days: int, growth_value: float):
        self.name = name
        self.height = height
        self.days = days
        self.growth_value = growth_value
    
    def show(self):
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.days} days old")

    def grow(self, days_passed: int):
        self.height += self.growth_value * days_passed

    def age(self, days_passed: int):
        self.grow(days_passed)
        self.days += days_passed


if __name__ == "__main__":
    names = ["rose", "sunflower", "cactus", "lily", "lavender"]
    heights = [25, 80, 15, 20, 15]
    days = [30, 45, 120, 30, 60]
    growth = [0.8, 2, 0.003, 1, 0.3]
    print("=== Plant Factory Output  ===")
    for i in range(0, 5):
        plant = Plant(names[i], heights[i], days[i], growth[i])
        print("Created: ", end="")
        plant.show()
    plant = None