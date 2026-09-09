class Plant:
    class _Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def _increment_grow(self):
            self._grow_calls += 1

        def _increment_age(self):
            self._age_calls += 1

        def _increment_show(self):
            self._show_calls += 1

        def display_status(self) -> str:
            return (f"Stats: {self._grow_calls} grow, "
                    f"{self._age_calls} age, {self._show_calls} show"
                    )

    def __init__(self, name: str, height: float, days: int,
                 growth_value: float):
        self.name = name
        self._height = height
        self._days = days
        self.growth_value = growth_value
        self.stats = self._Stats()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def get_plant_incomplete(cls) -> "Plant":
        return cls(name="unknown plant", height=0.0, days=0, growth_value=0.0)

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, new_height: float):
        if new_height < 0:
            print(f"{self.name.capitalize()}: "
                  "Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height:.1f}cm")

    @property
    def days(self) -> int:
        return self._days

    @days.setter
    def days(self, new_days: int):
        if new_days < 0:
            print(f"{self.name.capitalize()}: "
                  "Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = new_days
            print(f"Age updated: {self._days:.1f} days")

    @property
    def growth_value(self) -> float:
        return self._growth_value

    @growth_value.setter
    def growth_value(self, new_growth: float):
        if new_growth < 0:
            print(f"{self.name.capitalize()}: "
                  "Error, growth value can't be negative")
            print("Growth value update rejected")
        else:
            self._growth_value = new_growth

    def show(self):
        self.stats._increment_show()
        print(f"{self.name.capitalize()}: "
              f"{self.height:.1f}cm, {self.days} days old")

    def grow(self, days_passed: int):
        self.stats._increment_grow()
        self.height += self.growth_value * days_passed

    def age(self, days_passed: int):
        self.stats._increment_age()
        self.grow(days_passed)
        self.days += days_passed

    def get_statistics_str(self) -> str:
        return (
            f"[statistics for {self.name.capitalize()}]\n"
            f"{self.stats.display_status()}"
        )


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int,
                 growth_value: float, color: str, has_bloom: bool):
        super().__init__(name, height, days, growth_value)
        self.color = color
        self.has_bloom = has_bloom

    def show(self):
        self.stats._increment_show()
        bloom_status = (
            "is blooming beautifully"
            if self.has_bloom
            else "has not bloom yet"
        )
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.days} days old\n"
            f"Color: {self.color}\n"
            f"{self.name.capitalize()} {bloom_status}"
            f"\n{self.get_statistics_str()}"
        )

    def bloom(self):
        print(f"[asking the {self.name} to bloom]")
        self.has_bloom = True


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def _increment_shade(self) -> None:
            self._shade_calls += 1

        def display_status(self) -> str:
            base_status = super().display_status()
            return f"{base_status}, {self._shade_calls} shade"

    def __init__(self, name: str, height: float, days: int,
                 growth_value: float, trunk_diameter: float):
        super().__init__(name, height, days, growth_value)
        self.stats = self._TreeStats()
        self.trunk_diameter = trunk_diameter

    def show(self):
        self.stats._increment_show()
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.days} days old\n"
            f"Trunk diameter: {self.trunk_diameter:.1f}cm"
            f"\n{self.stats.display_status()}"
        )

    def produce_shade(self):
        self.stats._increment_shade()
        print(
            f"[asking the {self.name} to produce shade]\n"
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int,
                 growth_value: float, harvest_season: str,
                 nutritional_value: int):
        super().__init__(name, height, days, growth_value)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        self.stats._increment_show()
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.days} days old\n"
            f"Harvest season: {self.harvest_season.capitalize()}\n"
            f"Nutritional value: {self.nutritional_value}\n"
            f"\n{self.get_statistics_str()}"
        )

    def age(self, days_passed: int):
        super().age(days_passed)
        self.nutritional_value += days_passed


class Seed(Flower):

    def __init__(self, name: str, height: float, days: int,
                 growth_value: float, color: str, has_bloom: bool,
                 seeds: int):
        super().__init__(name, height, days, growth_value, color, has_bloom)
        self.seeds = seeds

    def bloom(self, seeds: int | None = None):
        super().bloom()
        if seeds is not None:
            self.seeds = seeds

    def show(self):
        bloom_status = (
            "is blooming beautifully"
            if self.has_bloom
            else "has not bloom yet"
        )
        self.stats._increment_show()
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.days} days old\n"
            f"Color: {self.color}\n"
            f"{self.name.capitalize()} {bloom_status}\n"
            f"Seeds: {self.seeds}"
            f"\n{self.get_statistics_str()}"
        )


def display_statistics(plant: Plant):
    print(plant.get_statistics_str())


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old ===")
    print("Is 30 days more than a year? -> "
          f"{Plant.is_older_than_year(30)}")
    print("Is 400 days more than a year? -> "
          f"{Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    flower = Flower("rose", 15, 10, 0.8, "red", False)
    flower.show()
    flower.grow(5)
    flower.bloom()
    flower.show()
    print("\n=== Tree")
    tree = Tree("oak", 200, 365, 0.54, 5)
    tree.show()
    tree.produce_shade()
    display_statistics(tree)

    print("\n=== Seed")
    seed = Seed("Sunflower", 80, 45, 2.1, "yellow", False, 0)
    seed.show()
    seed.age(20)
    seed.grow(20)
    seed.bloom(42)
    seed.show()

    print("\n=== Anonymous")
    anon = Plant.get_plant_incomplete()
    anon.show()
    display_statistics(anon)
